def count_max(seq):
    if seq == [0] or seq == (0, ):
        return 0
    new_seq = seq[:seq.index(0)]
    return new_seq.count(max(new_seq))


if __name__ == '__main__':
    assert count_max((1, 7, 9, 0)) == 1
    assert count_max((1, 3, 3, 1, 0)) == 2
    assert count_max((0, )) == 0


