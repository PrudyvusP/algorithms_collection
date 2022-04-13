def solution(strq: str) -> bool:
    strq = ''.join([i for i in strq if i.isalpha()])
    if strq == strq[::-1]:
        return True
    for x in strq:
        new_strq = strq.replace(x, '', 1)
        if new_strq == new_strq[::-1]:
            return True
    return False


if __name__ == '__main__':
    print(solution(input()))
    #print(solution('#14&*@(a)!(@14112)!@$)!@*$!*a)$*099'))
    assert solution('1kilg%rli8k') is True
    assert solution('kkkkkkkkkee') is False
    assert solution('#14&*@(a)!(@14112)!@$)!@*$!*a)$*099')
    assert solution('ekkkkkkkkkkkkkkkkkkkkkk')  == True
