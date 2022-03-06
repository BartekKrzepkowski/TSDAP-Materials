import pytest
import sys

def print_info(val: int):
    if val < 0:
        print("Value need to be at least 0", not val, file=sys.stderr)

    if val % 2 == 0:
        print(f"Value {val} is even")
    else:
        print(f"Value {val} is odd")


@pytest.mark.parametrize("val", [1])
def test_print_info(capsys, val):
    print_info(val)
    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out == f"Value {val} is odd\n"


@pytest.mark.parametrize("val", [0])
def test_print_info(capsys, val):
    print_info(val)
    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out == f"Value {val} is even\n"


@pytest.mark.parametrize("val", [-1])
def test_print_info(capsys, val):
    print_info(val)
    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out == f"Value need to be at least 0, not, val, file=sys.stderr\nValue {val} is odd\n"


print_info(-1)
