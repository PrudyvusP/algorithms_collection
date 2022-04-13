def street_time(seq):
    maxi = seq[0]
    for i in range(1, len(seq)):
        if seq[i] > maxi and seq[i] - maxi == 1:
            maxi = seq[i]
        else:
            return False
    return True


def solution(strq: str) -> str:
    cards = list(map(int, strq.split()))
    d = {}

    for card in cards:
        d[card] = d.get(card, 0) + 1
    if len(d) == 1:
        return "Шулер"
    d_d = {v: k for k, v in d.items()}
    if 4 in d_d:
        return "Каре"
    if 2 in d_d and 3 in d_d:
        return "Фулл Хаус"
    if street_time(sorted(cards)):
        return "Стрит"
    if 3 in d_d:
        return "Сет"
    if sorted(list(d.values())) == [1, 2, 2]:
        return "Две пары"
    if 2 in list(d.values()):
        return "Пара"
    return "Старшая карта"


if __name__ == '__main__':
    print(solution(input()))
    assert solution('5 5 5 5 5') == "Шулер"
    assert solution("5 5 5 5 4") == "Каре"
    assert solution('3 2 3 2 2') == "Фулл Хаус"
    assert solution('4 6 5 7 8') == "Стрит"
    assert solution('4 4 4 7 8') == "Сет"
    assert solution('10 10 11 11 1') == "Две пары"
    assert solution('10 10 1 2 3') == "Пара"
    assert solution('10 3 5 6 1') == "Старшая карта"

    # solution('4 6 5 7 8')
