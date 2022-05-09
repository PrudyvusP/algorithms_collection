def solution(arr_A, arr_B, arr_C):
    d = {}
    for i in range(1, len(arr_C)):
        d[arr_C[i]] = d.get(arr_C[i], []) + [i]
    for i in range(1, len(arr_A)):
        for j in range(1, len(arr_B)):
            if s - (arr_A[i] + arr_B[j]) in d:
                return i - 1, j - 1, d[s - (arr_A[i] + arr_B[j])][0] - 1
    return -1,


if __name__ == '__main__':
    s = int(input())
    arr_A = tuple(map(int, input().split()))
    arr_B = tuple(map(int, input().split()))
    arr_C = tuple(map(int, input().split()))
    print(*solution(arr_A, arr_B, arr_C))
