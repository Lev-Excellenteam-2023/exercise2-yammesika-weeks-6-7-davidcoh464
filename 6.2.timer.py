import time


def timer(func, *args, **k_args):
    """Calculate the runtime of function 'func' in milliseconds

    :param func: A function whose running time is measured
    :param args: positional arguments of function 'func'
    :param k_args: keyword arguments of function 'func'
    :return: runtime in milliseconds of 'func' on the passed arguments
    :rtype: float
    """
    start_time = time.perf_counter()
    func(*args, **k_args)
    end_time = time.perf_counter()
    return round((end_time - start_time) * 1000, 4)


if __name__ == '__main__':
    print(timer(zip, range(0, 4000), range(4000, 8000)))
    print(timer(len, range(pow(2, 31))))
