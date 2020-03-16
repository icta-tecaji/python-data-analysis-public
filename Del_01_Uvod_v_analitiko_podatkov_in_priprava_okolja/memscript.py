def my_func():
    a = [1] * 1000000
    b = [2] * 9000000
    del b
    return a
