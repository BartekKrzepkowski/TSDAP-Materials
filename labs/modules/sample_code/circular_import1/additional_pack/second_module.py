from sample_code.circular_import1.first_module import simple_fun1


def simple_fun2(n: int):
    return 2 + simple_fun1(n - 1)
