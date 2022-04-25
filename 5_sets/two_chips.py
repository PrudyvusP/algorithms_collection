def two_sum(seq, x):
    prev_nums_seq = set()
    for item in seq:
        if x - item in prev_nums_seq:
            return item, x - item
        prev_nums_seq.add(item)
    return None


if __name__ == '__main__':
    _ = input()
    nums = list(map(int, input().split()))
    x = int(input())
    if two_sum(nums, x):
        print(*two_sum(nums, x))
    else:
        print(two_sum(nums, x))
