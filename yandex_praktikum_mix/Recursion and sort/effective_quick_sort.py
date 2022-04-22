# ID 67615181
from collections import namedtuple


def partition(arr, low, high):
    """Makes partition of an array."""
    i, j = low, high
    pivot = arr[high]

    while i <= j:

        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return i, j


def quicksort(arr, low, high):
    """Quick sort in a place."""
    if low >= high:
        return -1
    i, j = partition(arr, low, high)
    quicksort(arr, low=low, high=j)
    quicksort(arr, low=i, high=high)


def timsort_in_action():
    """Timsort versus quicksort."""
    return sorted([input().split() for _ in range(int(input()))],
                  key=lambda x: (-int(x[1]), int(x[2]), x[0]))


if __name__ == '__main__':
    n = int(input())
    participants = [input().split() for _ in range(n)]
    Participant = namedtuple("Participant", "tasks fine name")
    participants = [
        Participant(-int(x[1]), int(x[2]), x[0]) for x in participants]
    quicksort(participants, low=0, high=n - 1)
    for participant in participants:
        print(participant.name)
