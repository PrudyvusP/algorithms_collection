def solution(strq):
    d = {}
    for i in strq:
        d[i] = d.get(i, 0) + 1
    odd = False
    for k, v in d.items():
        if v % 2:
            if odd is False:
                odd = True
            else:
                d[k] -= 1
    return sum(d.values())


def test():
    assert solution('qaaaaaaaab') == 9
    assert solution('ababqtd') == 5
    assert solution('bebebe') == 5
    assert solution('bebe') == 4


if __name__ == '__main__':
    test()
    print(solution(input()))
