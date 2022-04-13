def beegeek(num1: int, num2: int) -> str:
    res = []
    for i in range(num1, num2 + 1):
        if i % 3 == 0 and i % 7 == 0:
            res.append("BeeGeek")
        elif i % 3 == 0:
            res.append('Bee')
        elif i % 7 == 0:
            res.append('Geek')
        else:
            res.append(str(i))
    return ' '.join(res)


if __name__ == '__main__':
    assert beegeek(14, 21) == 'Geek Bee 16 17 Bee 19 20 BeeGeek'
    assert beegeek(1, 2) == '1 2'
    assert beegeek(10,
                   50) == '10 11 Bee 13 Geek Bee 16 17 Bee 19 20 BeeGeek 22 23 Bee 25 26 Bee Geek 29 Bee 31 32 Bee 34 Geek Bee 37 38 Bee 40 41 BeeGeek 43 44 Bee 46 47 Bee Geek 50'
