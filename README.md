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

# Viewing the html coverage report

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

# Coverage (experimental) - Not working yet



```
bazel coverage //:calculator_test
```