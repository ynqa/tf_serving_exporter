# Tensorflow Serving Exporter
[![Build Status](https://travis-ci.org/ynqa/tf_serving_exporter.svg?branch=master)](https://travis-ci.org/ynqa/tf_serving_exporter)

Prometheus exporter for [Tensorflow Serving](https://github.com/tensorflow/serving) metrics.

## Running

```
$ git clone https://github.com/ynqa/tf_serving_exporter.git
$ pip install -r requirements.txt
$ python tf_serving_exporter.py
```

For the config to run prometheus also, please refer to [example/prometeus.yml]( example/prometeus.yml).

## Usage

```
usage: tf_serving_exporter.py [-h] [--port PORT] [--tf_host TF_HOST]
                              [--tf_port TF_PORT]
                              [--model_name MODEL_NAME [MODEL_NAME ...]]
                              [--timeout TIMEOUT]
                              [--log_level {DEBUG,INFO,WARNING,ERROR}]

optional arguments:
  -h, --help            show this help message and exit
  --port PORT           port of exporter (default: 8500)
  --tf_host TF_HOST     host of tensorflow serving (default: localhost)
  --tf_port TF_PORT     port of tensorflow serving (default: 9000)
  --model_name MODEL_NAME [MODEL_NAME ...]
                        name of models (default: mnist)
  --timeout TIMEOUT     a duration of second to respond from tensorflow
                        serving (default: 1)
  --log_level {DEBUG,INFO,WARNING,ERROR}
                        log level (default: INFO)
```

## Metrics

|name|description|
|:--|:--|
|tf_serving_model_state|State of model name given|

### Metrics example

```
# HELP tf_serving_model_state model state on tf_serving
# TYPE tf_serving_model_state gauge
tf_serving_model_state{model_name="mnist",model_version="1"} 1.0
```
