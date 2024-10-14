import sys

def test_version():
    print(f"Python version: {sys.version}")
    assert sys.version_info[:2] == (3, 11), f"Expected Python 3.11, but got {sys.version}"