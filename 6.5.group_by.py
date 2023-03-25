def group_by(func, L):
    d = {}
    for i in L:
        x = func(i)
        if x in d:
            d[x].append(i)
        else:
            d[x] = [i]
    return d


if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))
