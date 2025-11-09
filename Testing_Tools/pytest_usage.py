'''
Built-in pytest module usage showcase.

Different from unittest, there's no need to define any class from the user's side:
defining some functions is enough.

Use "pytest" command from the CLI:
pytest -v                                   # Run all tests verbosely in the module (verbose mode). Execute while into target directory.
pytest tests/test_math_utils.py -v          # Run tests in a specific file
pytest tests/test_math_utils.py::test_div   # Run a specific test function
pytest --maxfail=1 -v                       # Stop after first failure
pytest -s -v                                # Show print() output and debug messages

Install it with "pip install pytest" if necessary.
'''

import pytest
from math_ops import add, mul, sub, div

def test_add():
    assert add(2, 3) == 5
    assert add(1.2, 3.4) == 4.6

def test_mul():
    assert mul(2, 3) == 6
    assert mul(1.2, 3.4) == 4.08

def test_sub():
    assert sub(2, 3) == -1
    assert sub(1.2, 3.4) == -2.2

def test_div():
    assert div(10, 2) == 5
    assert pytest.approx(div(6.6, 2)) == 3.3
    with pytest.raises(ZeroDivisionError):
        div(1, 0)