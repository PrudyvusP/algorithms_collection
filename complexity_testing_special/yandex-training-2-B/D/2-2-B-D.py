def legs_to_be_left(l, k, seq):
    pass


if __name__ == '__main__':
    assert legs_to_be_left(5, 2, [0, 2]) == (2, )
    assert legs_to_be_left(13, 4, [1, 4, 8, 11]) == (4, 8)
    assert legs_to_be_left(14, 6, [1, 6, 8, 11, 12, 13]) == (6, 8)
