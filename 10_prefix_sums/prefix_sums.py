import sys


def create_prefix_sums(arr):
    result = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        result[i] = result[i - 1] + arr[i - 1]
    return result


def rsq(prefix_sum_arrr, left=0, right=None):
    right = right or len(prefix_sum_arrr)
    return prefix_sum_arrr[right] - prefix_sum_arrr[left - 1]


def test():
    arr = [1, 2, 3, 4]
    prefixes = create_prefix_sums(arr)
    assert rsq(prefixes, 1, 1) == 1
    assert rsq(prefixes, 1, 2) == 3
    assert rsq(prefixes, 1, 3) == 6


if __name__ == '__main__':
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    prefixes = create_prefix_sums(arr)
    for _ in range(q):
        left, right = map(int, sys.stdin.readline().rstrip().split())
        print(rsq(prefixes, left, right))
