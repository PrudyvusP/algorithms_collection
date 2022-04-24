def solution(strq: str) -> bool:
    strq = ''.join([i for i in strq if i.isalpha()])
    if strq == strq[::-1]:
        return True
    for x in strq:
        new_strq = strq.replace(x, '', 1)
        if new_strq == new_strq[::-1]:
            return True
    return False


strq = ''.join([x for x in input() if x.isalpha()])
while strq != '':
    #print(s)
    if strq[0] == strq[-1]:
        strq = strq[1:-1]
    else:
        print(strq)
        print('here')
        a = strq[:-1]
        print(a)
        b = strq[1:]
        print(b)
        if a == a[::-1] or b == b[::-1]:
            print(True)
        else:
            print(False)
        break
else:
    print(True)

"""    
if __name__ == '__main__':
    print(solution(input()))
    assert solution('1kilg%rli8k') is True
    assert solution('kkkkkkkkkee') is False
    assert solution('#14&*@(a)!(@14112)!@$)!@*$!*a)$*099')
    assert solution('ekkkkkkkkkkkkkkkkkkkkkk') is True
"""