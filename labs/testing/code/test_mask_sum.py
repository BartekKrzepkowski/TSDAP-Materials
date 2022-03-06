import pytest
import numpy as np


def mask_sum(data, mask):
    res = 0
    for val, mask_val in zip(data, mask):
       if mask_val != 0:
            res += val
    return res

@pytest.mark.parametrize("data", [[5, 3, 2]])
@pytest.mark.parametrize("mask", [[1, 0, 1]])
def test_mask_sum(data, mask):
    assert mask_sum(data, mask) == 7