from tensorflow_serving.apis import get_model_status_pb2
from tf_serving_exporter import model_available

def test_model_available():
    available_state = get_model_status_pb2.ModelVersionStatus.AVAILABLE
    assert model_available(available_state)
    loading_state = get_model_status_pb2.ModelVersionStatus.LOADING
    assert model_available(loading_state) == False
