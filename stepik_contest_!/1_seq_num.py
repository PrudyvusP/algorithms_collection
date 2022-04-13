def solution(num: int):
    x = 1
    res = []
    while len(res) <= num:
        for _ in range(1, x + 1):
            res.append(str(x))
        x += 1
    return ' '.join(res[:num])


if __name__ == '__main__':
    print(solution(int(input())))
    # assert solution(1) == '1'
    # assert solution(7) == '1 2 2 3 3 3 4'
    # assert solution(10) == '1 2 2 3 3 3 4 4 4 4'
