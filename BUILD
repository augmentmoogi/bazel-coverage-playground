load("@deps//:requirements.bzl", "requirement")
load("@rules_python_pytest//python_pytest:defs.bzl", "py_pytest_test")

py_binary(
    name = "calculator",
    srcs = ["calculator.py"],
)

# pytest_test(
#     name = "str_utils_test",
#     srcs = ["str_utils_test.py"],
#     deps = [
#         ":str_utils",
#         requirement("pytest"),
#     ],
# )

py_pytest_test(
    name = "calculator_test",
    size = "small",
    srcs = ["calculator_test.py"],
    deps = [
        ":calculator",
        requirement("pytest"),
    ],
)
