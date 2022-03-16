def moving_average_naive(seq: list, k: int) -> list:
    result = []
    for i in range(0, len(seq) - k + 1):
        end_index = i + k
        current_sum = 0
        for j in seq[i:end_index]:
            current_sum += j
        current_avg = current_sum / k
        result.append(current_avg)
    return result


def moving_average(seq: list, k: int) -> list:
    result = []
    current_sum = sum(seq[0:k])
    result.append(current_sum / k)
    for i in range(0, len(seq) - k):
        current_sum -= seq[i]
        current_sum += seq[i + k]
        current_avg = current_sum / k
        result.append(current_avg)
    return result


assert moving_average([1, 2, 3, 4, 5, 6, 7], 4) == [2.5, 3.5, 4.5, 5.5]
#assert moving_average([9, 3, 2, 0, 1, 5, 1, 0, 0], 3) == [4.6666666667, 1.666666667, 1, 2, 2.333333335, 2, 0.3333333]
assert moving_average([1, 2, 3, 4, 5], 5) == [3, ]
