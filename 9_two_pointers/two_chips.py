def twosum_with_sort(numbers, x):
    numbers.sort()
    left = 0
    right = len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == x:
            return numbers[left], numbers[right]
        if current_sum < x:
            left += 1
        else:
            right -= 1
    return None


def test():
    assert twosum_with_sort([15, 2, 3, 4, 5, 0, 33], 6) == (2, 4)
    assert twosum_with_sort([], 6) is None
    assert twosum_with_sort([1], 1) is None
    assert twosum_with_sort([1, 2], 3) == (1, 2)


if __name__ == '__main__':
    _ = input()
    nums = list(map(int, input().split()))
    x = int(input())
    if twosum_with_sort(nums, x):
        print(*twosum_with_sort(nums, x))
    else:
        print(twosum_with_sort(nums, x))
