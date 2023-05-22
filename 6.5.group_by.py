def group_by1(func, list_objects):
    result = {}
    {result.setdefault(func(obj), []).append(obj) for obj in list_objects}
    return result


def group_by2(func, list_objects):
    return {func(obj): list(filter(lambda value: func(value) == func(obj), list_objects)) for obj in list_objects}


if __name__ == '__main__':
    print(group_by1(sum, [[1, 2, 3], [3, 3], [4, 4, 4], [8, 4], [6], [111]]))
    print(group_by2(sum, [[1, 2, 3], [3, 3], [4, 4, 4], [8, 4], [6], [111]]))
    # {6: [[1, 2, 3], [3, 3], [6]], 12: [[4, 4, 4], [8, 4]], 111: [[111]]}

