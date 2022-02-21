def count_min(strq):
    if len(strq) == 1:
        return 0
    counter = 0
    for i in range(len(strq) // 2):
        if strq[i] != strq[-i - 1]:
            counter += 1
    return counter


if __name__ == '__main__':
    assert count_min('a') == 0
    assert count_min('ab') == 1
    assert count_min('cognitive') == 4
