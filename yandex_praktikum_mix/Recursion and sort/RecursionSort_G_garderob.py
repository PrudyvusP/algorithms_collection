def counting_sort(array):
    counted_values = [0] * 3
    for value in array:
        counted_values[value] += 1
    return counted_values


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    r = counting_sort(arr)
    for i in range(3):
        print((str(i) + ' ') * r[i], end='')
