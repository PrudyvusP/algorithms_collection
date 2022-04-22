def is_odd(n):
    return n % 2 != 0


def legs_to_be_left(l, k, seq):
    if k == 1:
        return seq[0]

    center = l // 2
    if is_odd(l) and center in set(seq):
        return center,
    i = 0
    while True:
        if seq[i] >= center:
            return seq[i - 1], seq[i]
        i += 1


if __name__ == '__main__':
    assert legs_to_be_left(5, 2, [0, 2]) == (2,)
    assert legs_to_be_left(13, 4, [1, 4, 8, 11]) == (4, 8)
    assert legs_to_be_left(14, 6, [1, 6, 8, 11, 12, 13]) == (6, 8)
    assert legs_to_be_left(4, 4, [0, 1, 2, 3]) == (1, 2)
    assert legs_to_be_left(6, 3, [0, 1, 3]) == (1, 3)
