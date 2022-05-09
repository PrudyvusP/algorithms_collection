def create_prefix_sum(nums):
    prefixsum = [0] * (len(nums) + 1)
    mini = -1 * 10 ** 9
    min_prefix_sum = 0
    for i in range(1, len(nums) + 1):
        prefixsum[i] = prefixsum[i - 1] + nums[i - 1]
        mini = max(mini, prefixsum[i] - min_prefix_sum)
        min_prefix_sum = min(min_prefix_sum, prefixsum[i])
    return mini


def solution2(arr):
    i = 0
    summa = 0
    maxi = arr[0]
    while i < len(arr):
        summa += arr[i]
        if summa < 0:
            summa = 0
        else:
            if summa >= maxi:
                maxi = summa
        i += 1
    return maxi


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    print(solution2(nums))
