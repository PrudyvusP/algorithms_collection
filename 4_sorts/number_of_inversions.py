inversion_count = 0


def merge(arr1, arr2):
    global inversion_count
    len_1, len_2 = len(arr1), len(arr2)
    result = [None] * (len_1 + len_2)
    i, j, k = 0, 0, 0
    while i < len_1 and j < len_2:
        if arr1[i] <= arr2[j]:
            result[k] = arr1[i]
            i += 1
        else:
            inversion_count += len_1 - i
            result[k] = arr2[j]
            j += 1
        k += 1
    while i < len_1:
        result[k] = arr1[i]
        i += 1
        k += 1
    while j < len_2:
        result[k] = arr2[j]
        j += 1
        k += 1
    return result


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


if __name__ == '__main__':
    _ = int(input())
    arr = list(map(int, input().split()))
    merge_sort(arr)
    print(inversion_count)
