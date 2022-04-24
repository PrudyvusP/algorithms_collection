def solution(seq) -> None:
    flag = False
    is_sorted = True
    for _ in range(len(seq)):
        for index in range(1, len(seq)):
            if seq[index] < seq[index-1]:
                flag = True
                seq[index-1], seq[index] = seq[index], seq[index-1]
                is_sorted = False
        if flag:
            print(*seq)
        flag = False
    if is_sorted:
        print(*seq)


if __name__ == '__main__':
    _, seq = input(), list(map(int, input().split()))
    solution(seq)
