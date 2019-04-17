def my_func():
    a = [1] * 100000
    b = [2] * 900000
    del b
    return a
