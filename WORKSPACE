workspace(name = "tf_serving_exporter")

tensorflow_serving_version = "0d219b72c01d45af8c5d8079950b09df839d9e15"
rules_docker_version = "0.4.0"
rules_python_version = "115e3a0dab4291184fdcb0d4e564a0328364571a"

# Docker rules.
http_archive(
    name = "io_bazel_rules_docker",
    url = "https://github.com/bazelbuild/rules_docker/archive/v%s.tar.gz" % rules_docker_version,
    strip_prefix = "rules_docker-%s" % rules_docker_version,
    sha256 = "6dede2c65ce86289969b907f343a1382d33c14fbce5e30dd17bb59bb55bb6593",
)

load(
    "@io_bazel_rules_docker//python:image.bzl",
    _py_image_repos = "repositories",
)
_py_image_repos()

# Python rules.
http_archive(
    name = "io_bazel_rules_python",
    url = "https://github.com/bazelbuild/rules_python/archive/%s.tar.gz" % rules_python_version,
    strip_prefix = "rules_python-%s" % rules_python_version,
    sha256 = "0d1810fecc1bf2b6979d2af60e157d93d3004805bd8b7fda6eb52dda13480dca",
)

load("@io_bazel_rules_python//python:pip.bzl", "pip_repositories", "pip_import")
pip_repositories()
pip_import(
    name = "python_default_library",
    requirements = "//:requirements.txt"
)

load("@python_default_library//:requirements.bzl", "pip_install")
pip_install()

# Tensorflow serving.
http_archive(
    name = "tf_serving",
    sha256 = "9891a4567401e16e691628c2f6199f9c69fc77a71d565aad62e04bbc1d972182",
    strip_prefix = "serving-%s" % tensorflow_serving_version,
    url = "https://github.com/tensorflow/serving/archive/%s.tar.gz" % tensorflow_serving_version,
)
load("@tf_serving//tensorflow_serving:repo.bzl", "tensorflow_http_archive")

tensorflow_http_archive(
    name = "org_tensorflow",
    sha256 = "dd44550909aab50790495264d3e5c9e9373f9c0f0272047fd68df3e56c07cc78",
    git_commit = "7a212edc6b3ed6200158fe51acf4694a62ca6938",
)

http_archive(
    name = "io_bazel_rules_closure",
    sha256 = "dbe0da2cca88194d13dc5a7125a25dd7b80e1daec7839f33223de654d7a1bcc8",
    strip_prefix = "rules_closure-ba3e07cb88be04a2d4af7009caa0ff3671a79d06",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_closure/archive/ba3e07cb88be04a2d4af7009caa0ff3671a79d06.tar.gz",
        "https://github.com/bazelbuild/rules_closure/archive/ba3e07cb88be04a2d4af7009caa0ff3671a79d06.tar.gz",  # 2017-10-31
    ],
)
load("@tf_serving//tensorflow_serving:workspace.bzl", "tf_serving_workspace")
tf_serving_workspace()
