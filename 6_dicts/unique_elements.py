
if __name__ == '__main__':
    lst = list(map(int, input().split()))
    counter = {}
    for i in lst:
        counter[i] = counter.get(i, 0) + 1
    print(*(key for key in counter if counter[key] == 1))
