import math
import sys
import pytest
import regex

py_version = float(regex.search(r'^\d\.\d+', sys.version).group())


@pytest.mark.skipif(py_version < 3.8, reason='Python 3.7 or less')
@pytest.mark.parametrize('p', [[0]])
@pytest.mark.parametrize('q', [[0]])
def test_math_dist(p, q):
    math.dist(p, q) == 0