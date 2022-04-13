def solution(seq, cost):
    seq = list(map(int, seq.split()))
    return bin_search(seq, cost, 0, len(seq))


def bin_search(seq, x, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if seq[mid] == x:
        return mid
    elif x < seq[mid]:
        return bin_search(seq, x, left, mid)
    else:
        return bin_search(seq, x, mid + 1, right)


def recurs(array, price, left, right):
    if left >= right and left != 0:
        return -1
    mid = (left + right) // 2
    if array[mid] >= price and (array[mid - 1] < price or mid == 0):
        return mid + 1
    elif array[mid] < price:
        return recurs(array, price, mid + 1, right)
    else:
        return recurs(array, price, left, mid)


def test():
    assert solution('1 2 4 4 6 8', 3) == '3 5'
    assert solution('1 2 4 4 4 4', 3) == '3 -1'
    assert solution('1 2 4 4 4 4', 10) == '-1 -1'


if __name__ == '__main__':
    print(solution('1 2 4 4 4 4', 3))
