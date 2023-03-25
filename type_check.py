import functools


def type_check(correct_type):
    def type_check_decorator(func):
        @functools.wraps(func)
        def wrapper(arg):
            if type(arg) != correct_type:
                raise TypeError(f"Expected {correct_type}, but got {type(arg)} instead")
            return func(arg)
        return wrapper
    return type_check_decorator


@type_check(int)
def times2(num):
    return num * 2


if __name__ == '__main__':
    try:
        print(times2(3))
        print(times2("3"))
    except Exception as inst:
        print(inst)
