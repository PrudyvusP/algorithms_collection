def min_time(seq):
    return sum(seq) - max(seq)


if __name__ == '__main__':
    assert min_time([2, 1]) == 1
    assert min_time([10]) == 0
    assert min_time([1, 2, 3, 4, 5]) == 10
