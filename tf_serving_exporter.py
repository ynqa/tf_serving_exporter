import argparse
import time
import logging

import grpc
from grpc.framework.interfaces.face.face import AbortionError, ExpirationError

from prometheus_client import start_http_server, REGISTRY
from prometheus_client.core import GaugeMetricFamily

from tensorflow_serving.apis import get_model_status_pb2, model_service_pb2_grpc


def model_available(state):
    return state == get_model_status_pb2.ModelVersionStatus.AVAILABLE


class TFServingExporter(object):
    """
    Export the metrics of tensorflow serving.

    Args:
        stub: Stub of gRPC client.
        model_name: List of model name.
        timeout: A duration of time to respond from tensorflow serving.
    """

    def __init__(self, stub, model_name, timeout):
        self.stub = stub
        self.model_name = model_name
        self.timeout = timeout

    def collect(self):
        metric = GaugeMetricFamily(
            name='tf_serving_model_state',
            documentation='model state on tf_serving',
            labels=['model_name', 'model_version'])

        for n in self.model_name:
            # create request
            request = get_model_status_pb2.GetModelStatusRequest()
            request.model_spec.name = n
            try:
                result_future = self.stub.GetModelStatus.future(
                    request, self.timeout)
                model_version_status = result_future.result(
                ).model_version_status
            except AbortionError as e:
                logging.exception(
                    'AbortionError on GetModelStatus of {}: {}'.format(
                        n, e.details))
            except Exception as e:
                logging.exception(
                    'Exeption on GetModelStatus of {}: {}'.format(
                        n, e))
            else:
                # success to connect to serving
                for model in model_version_status:
                    metric.add_metric(
                        labels=[n, str(model.version)],
                        value=int(model_available(model.state)))
                    logging.debug(
                        'Add metric: name:{}, version:{}, state:{}'.format(
                            n, model.version, model.state))
                yield metric


def main(args):
    # apply logging config
    logging.basicConfig(
        format='[%(asctime)s] %(levelname)s %(message)s', level=args.log_level)

    # create channel and stub
    channel = grpc.insecure_channel('{}:{}'.format(args.tf_host, args.tf_port))
    stub = model_service_pb2_grpc.ModelServiceStub(channel)

    # register tf_serving exporter
    REGISTRY.register(TFServingExporter(stub, args.model_name, args.timeout))

    start_http_server(args.port)
    logging.info('Server started on port:{}'.format(args.port))
    while True:
        time.sleep(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--port',
        type=int,
        default=8500,
        help='port of exporter (default: 8500)')
    parser.add_argument(
        '--tf_host',
        type=str,
        default='localhost',
        help='host of tensorflow serving (default: localhost)')
    parser.add_argument(
        '--tf_port',
        type=int,
        default=9000,
        help='port of tensorflow serving (default: 9000)')
    parser.add_argument(
        '--model_name',
        type=str,
        nargs='+',
        default=['mnist'],
        help='name of models (default: mnist)')
    parser.add_argument(
        '--timeout',
        type=float,
        default=1,
        help=
        'a duration of second to respond from tensorflow serving (default: 1)')
    parser.add_argument(
        '--log_level',
        type=str,
        default='INFO',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        help='log level (default: INFO)')
    main(parser.parse_args())
