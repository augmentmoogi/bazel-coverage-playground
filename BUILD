load("@deps//:requirements.bzl", "requirement")
load("@rules_python_pytest//python_pytest:defs.bzl", "py_pytest_test")

py_binary(
    name = "calculator",
    srcs = ["calculator.py"],
)

py_test(
    name = "calculator_test2",
    size = "small",
    srcs = ["calculator_test2.py"],
    deps = [
        ":calculator",
    ],
)

py_pytest_test(
    name = "calculator_test",
    size = "small",
    srcs = ["calculator_test.py"],
    deps = [
        ":calculator",
        requirement("pytest"),
        requirement("pytest-cov"),
    ],
)

py_pytest_test(
    name = "python_version_test",
    srcs = ["python_version_test.py"],
)

py_library(
    name = "my_calculator",
    srcs = ["my_calculator/my_calculator.py"],
)

py_test(
    name = "my_calculator_test",
    size = "small",
    srcs = ["my_calculator/my_calculator_test.py"],
    deps = [
        ":my_calculator",
    ],
)
