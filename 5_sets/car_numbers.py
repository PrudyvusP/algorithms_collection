n = int(input())
test_words = [set(input().strip()) for _ in range(n)]
k = int(input())
nums = []
max_count = 0

for i in range(k):
    num = input().strip()
    num_set = set(num)
    count = 0
    for test_word in test_words:
        if test_word.issubset(num_set):
            count += 1
    nums.append((num, count))
    max_count = max(max_count, count)

ans = []
for num in nums:
    if num[1] == max_count:
        ans.append(num[0])
print(*ans, sep='\n')
