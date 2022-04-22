from typing import List, Optional


def bin_search(arr: List[int],
               target: int = 0,
               left: int = 0,
               right: Optional[int] = None
               ) -> int:
    """Bin search by a target on unique arr values."""
    right = right or len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def get_pivot(arr: List[int],
              left: int = 0,
              right: Optional[int] = None
              ) -> int:
    """Bin search on unique arr values."""
    right = right or len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= arr[right]:
            left = mid + 1
        else:
            right = mid
    return right or len(arr) - 1


def broken_search(arr: List[int],
                  target: int = 0
                  ) -> int:
    """Bin search with two sorted arrays with unique values."""
    pivot = get_pivot(arr)

    if arr[pivot] == target:
        return pivot

    if arr[0] <= target:
        return bin_search(arr, target, right=pivot - 1)
    return bin_search(arr, target, left=pivot + 1)


def test():
    """List of asserts to check funcs logic."""
    assert bin_search([1, 4, 5, 8, 9, 11, 17, 25], 1) == 0
    assert get_pivot([19, 21, 100, 101, 1, 4, 5, 7, 12]) == 4
    assert broken_search([19, 21, 100, 101, 1, 4, 5, 7, 12], 5) == 6
