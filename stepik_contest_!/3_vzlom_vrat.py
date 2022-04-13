def solution(strq1: str, strq2: str) -> str:
    symb_set = set(strq2) - set(strq1)
    if symb_set:
        return "".join(symb_set)
    strq1 = sorted(list(strq1))
    strq2 = sorted(list(strq2))
    for i in range(len(strq1)):
        if strq1[i] != strq2[i]:
            return strq2[i]
    return strq2[-1]


if __name__ == '__main__':
    print(solution(input(), input()))
    assert solution('tuturu', 'tuturuu') == 'u'
    assert solution('スーパーハカー', 'スーパーハッカー') == 'ッ'
