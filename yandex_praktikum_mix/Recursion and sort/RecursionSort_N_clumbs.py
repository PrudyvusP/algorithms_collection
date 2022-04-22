n = int(input())
result = sorted([tuple(map(int, input().split())) for _ in range(n)])

l = result[0][0]
r = result[0][1]
i = 1

while i < n:
    if result[i][0] > r:
        print(l, r)
        l = result[i][0]
        r = result[i][1]
    elif result[i][1] > r:
        r = result[i][1]
    i += 1
print(l, r)
