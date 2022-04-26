def merge(arr, lf, mid, rg) -> list:
    array_1 = arr[lf:mid]
    array_2 = arr[mid:rg+1]
    len_1 = mid - lf
    len_2 = rg - mid
    i = j = k = 0

    while i < len_1 and j < len_2:
        if array_1[i] < array_2[j]:
            arr[k] = array_1[i]
            i += 1
        else:
            arr[k] = array_2[j]
            j += 1
        k += 1

    while i < len_1:
        arr[k] = array_1[i]
        i += 1
        k += 1
    while j < len_2:
        arr[k] = array_2[j]
        j += 1
        k += 1

    return arr


def merge_sort(arr, lf, rg):
    if len(arr) == 1:
        return arr
    mid = (lf + rg) // 2
    left = merge_sort(arr[lf:mid], lf, mid)
    right = merge_sort(arr[mid:rg+1], mid, rg)
    merge(left, right)





def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    #print(b)
    print(merge_sort())
    #expected = [1, 2, 4, 9, 10, 11]

    #print(b, expected)
    #assert b == expected


    #c = [1, 4, 2, 10, 1, 2]
    #merge_sort(c, 0, 6)
    #expected = [1, 1, 2, 2, 4, 10]
    #assert c == expected
    #print(c, expected)
"""

Функция merge_sort принимает некоторый подмассив, который нужно отсортировать.
 Подмассив задаётся полуинтервалом — его началом и концом.
  Функция должна отсортировать передаваемый в неё подмассив, она ничего не возвращает.
  
Функция merge_sort разбивает полуинтервал на две половинки и рекурсивно вызывает сортировку отдельно для каждой.
 Затем два отсортированных массива сливаются в один с помощью merge.

"""
"""
def merge_sort(arr, left, right):
    if left >= right:
        return

    mid = (left + right)//2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge(arr, left, right, mid)


    def merge(arr, left, right, mid):
        left_sublist = arr[left:mid + 1]
        right_sublist = arr[mid+1:right+1]
        left_sublist_index = 0
        right_sublist_index = 0
        sorted_index = left
        while left_sublist_index < len(left_sublist) and right_sublist_index < len(right_sublist):
            if left_sublist[left_sublist_index] <= right_sublist[right_sublist_index]:
                arr[sorted_index] = left_sublist[left_sublist_index]
                left_sublist_index = left_sublist_index + 1
            else:
                arr[sorted_index] = right_sublist[right_sublist_index]
                right_sublist_index = right_sublist_index + 1
            sorted_index = sorted_index + 1

            while left_sublist_index < len(left_sublist):
                arr[sorted_index] = left_sublist[left_sublist_index]
                left_sublist_index = left_sublist_index + 1
                sorted_index = sorted_index + 1

            while right_sublist_index < len(right_sublist):
                arr[sorted_index] = right_sublist[right_sublist_index]
                right_sublist_index = right_sublist_index + 1
                sorted_index = sorted_index + 1
        return arr

"""
if __name__ == '__main__':
    test()
