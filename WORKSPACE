## Add python rules (mainly for pip)

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    sha256 = "778aaeab3e6cfd56d681c89f5c10d7ad6bf8d2f1a72de9de55b23081b2d31618",
    strip_prefix = "rules_python-0.34.0",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.34.0/rules_python-0.34.0.tar.gz",
)

load("@rules_python//python:repositories.bzl", "py_repositories")

py_repositories()



## Install pip dependencies. TODO: use lock file.
load("@rules_python//python:pip.bzl", "pip_parse")

pip_parse(
    name = "deps",
    requirements_lock = ":requirements.lock",
)

load("@deps//:requirements.bzl", "install_deps")

install_deps()

## pytest

http_archive(
    name = "rules_python_pytest",
    sha256 = "e2556404ef56ea3ec938597616afc51d78e1832cfe511b196e9f2b8fd7f8f149",
    strip_prefix = "rules_python_pytest-1.1.1",
    url = "https://github.com/caseyduquettesc/rules_python_pytest/releases/download/v1.1.1/rules_python_pytest-v1.1.1.tar.gz",
)

load("@rules_python_pytest//python_pytest:repositories.bzl", "rules_python_pytest_dependencies")

rules_python_pytest_dependencies()
