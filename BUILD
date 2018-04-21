load("@python_default_library//:requirements.bzl", "requirement")
load("@io_bazel_rules_docker//python:image.bzl", "py_image")
load("@io_bazel_rules_docker//container:container.bzl", "container_push")

py_binary(
    name = "tf_serving_exporter",
    srcs = ["tf_serving_exporter.py"],
    main = "tf_serving_exporter.py",
    deps = [
        requirement("grpcio"),
        requirement("prometheus_client"),
        "@tf_serving//tensorflow_serving/apis:get_model_status_proto_py_pb2",
        "@tf_serving//tensorflow_serving/apis:model_service_proto_py_pb2",
    ],
)

py_image(
    name = "tf_serving_exporter_image",
    srcs = ["tf_serving_exporter.py"],
    main = "tf_serving_exporter.py",
    deps = [
        "@tf_serving//tensorflow_serving/apis:get_model_status_proto_py_pb2",
        "@tf_serving//tensorflow_serving/apis:model_service_proto_py_pb2",
    ],
)

container_push(
    name = "push_image",
    image = ":tf_serving_exporter_image",
    format = "Docker",
    registry = "index.docker.io",
    repository = "ynqa/tf_serving_exporter",
    tag = "{DOCKER_TAG}"
)
