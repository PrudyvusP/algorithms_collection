def get_points() -> int:
    k = int(input())
    nums = {}

    for i in range(4):
        line = input().rstrip()
        for symb in line:
            if symb.isdigit():
                nums[symb] = nums.get(symb, 0) + 1

    return len([key for key in nums if nums[key] <= k * 2])


if __name__ == '__main__':
    print(get_points())
