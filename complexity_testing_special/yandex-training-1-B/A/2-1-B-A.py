def get_verdict(code, interator, checker):
    if interator == 0:
        if code != 0:
            return 3
        return checker
    elif interator == 1:
        return checker
    elif interator == 4:
        if code != 0:
            return 3
        return 4
    elif interator == 6:
        return 0
    elif interator == 7:
        return 1
    return interator


if __name__ == '__main__':
    assert (get_verdict(0, 0, 0)) == 0
    assert (get_verdict(-1, 0, 1)) == 3
    assert (get_verdict(42, 1, 6)) == 6
    assert (get_verdict(44, 7, 4)) == 1
    assert (get_verdict(1, 4, 0)) == 3
    assert (get_verdict(-3, 2, 4)) == 2
