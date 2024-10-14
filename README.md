For now - you need to run pip by yourself.


```
pip install pip-tools
pip-compile requirements.txt -o requirements.lock
```


If you want to run scripts outside of bazel do

```
pip install -r requirements.lock
```


# Using Python

We recommend you use a python environment.

In VSCode this means to install the python plugin, and running the shell from an environment.

# Running tests in pytest (outside of bazel)

```
pytest calculator_test.py
```

Running with test coverage

```
pytest --cov=calculator calculator_test.py --cov-report=html
```

## Viewing the html coverage report (outside of bazel)

We recommend to use the project `serve`

```
npm install -g serve
```

```
serve htmlcov
```

Then you should be able to visit

```
http://localhost:3000/index.html
```

To view the results.

# Coverage (without pytest)

In order to get coverage to work I had to modify the toolchain in `MODULE.bazel`

```
python.toolchain(
    python_version = "3.11",
    configure_coverage_tool = True,
    is_default = True,
)
```

Then - I defined a test without pytest.

Then I ran the following command

```
bazel coverage //:my_calculator_test --combined_report=lcov --test_output=all --instrumentation_filter=// --nocache_test_results
```

To generate an HTML report for it I ran

```
genhtml --branch-coverage --output genhtml "$(bazel info output_path)/_coverage/_coverage_report.dat"
```

The report is in `genhtml` - use `serve` to view it.


# Pytest + Coverage (experimental) - Not working yet

NOTE (10/13/2024): This is currently failing due to a version issue with `pytest-cov` and `coverage`.

```
bazel coverage //:calculator_test
```


# Python Version

Instructions: `https://rules-python.readthedocs.io/en/latest/toolchains.html`

We define

```
bazel_dep(name="rules_python", version=...)
python = use_extension("@rules_python//python/extensions:python.bzl", "python")

python.toolchain(python_version = "3.12", is_default = True)
```

The version is available in the [github project](https://github.com/bazelbuild/rules_python)


[My SO Answer](https://stackoverflow.com/a/79084901/1068746)

