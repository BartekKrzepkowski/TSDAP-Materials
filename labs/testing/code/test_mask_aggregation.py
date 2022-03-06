import pytest
import operator
from typing import Callable, List


def mask_aggregation(agg_operator: Callable[[float, float], float], data: List[float], mask: List[bool]) -> float:
    res = 0
    for val, mask_val in zip(data, mask):
       if mask_val != 0:
            res = agg_operator(res, val)
    return res


@pytest.mark.parametrize("agg_operator", [operator.add])
@pytest.mark.parametrize("data", [[5, 3, 2]])
@pytest.mark.parametrize("mask", [[1, 0, 1]])
@pytest.mark.parametrize("result", [7])
def test_mask_sum1(agg_operator, data, mask, result):
    assert mask_aggregation(agg_operator, data, mask) == result


@pytest.mark.parametrize("agg_operator", [operator.and_])
@pytest.mark.parametrize("data", [[True, False, True]])
@pytest.mark.parametrize("mask", [[1, 1, 1]])
@pytest.mark.parametrize("result", [False])
def test_mask_and_(agg_operator, data, mask, result):
    assert mask_aggregation(agg_operator, data, mask) == result


@pytest.mark.parametrize("agg_operator", [operator.or_])
@pytest.mark.parametrize("data", [[True, False, True]])
@pytest.mark.parametrize("mask", [[1, 1, 1]])
@pytest.mark.parametrize("result", [True])
def test_mask_or_(agg_operator, data, mask, result):
    assert mask_aggregation(agg_operator, data, mask) == result
