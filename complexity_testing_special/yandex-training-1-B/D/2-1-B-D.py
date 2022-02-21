def place_school(n, lst):
    if not n or not lst:
        return 0
    return lst[len(lst) // 2]


if __name__ == '__main__':
    assert place_school(4, [1, 2, 3, 4]) == 3
    assert place_school(3, [-1, 0, 1]) == 0
