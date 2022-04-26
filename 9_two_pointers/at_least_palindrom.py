def solution(strq: str) -> bool:
    strq = ''.join([x for x in strq if x.isalpha()])
    while strq != '':
        if strq[0] == strq[-1]:
            strq = strq[1:-1]
        else:
            a = strq[:-1]
            b = strq[1:]
            if a == a[::-1] or b == b[::-1]:
                return True
            return False
    else:
        return True


if __name__ == '__main__':
    strq = input()
    print(solution(strq))
    assert solution('1kilg%rli8k') is True
    assert solution('kkkkkkkkkee') is False
    assert solution('#14&*@(a)!(@14112)!@$)!@*$!*a)$*099') is True
    assert solution('ekkkkkkkkkkkkkkkkkkkkkk') is True
