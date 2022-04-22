def get_nearest_point(d, x, y):
    if x >= 0 and y >= 0 and x + y <= d:
        return 0
    dist = [
        (x ** 2 + y ** 2, 1),
        ((x - d) ** 2 + y ** 2, 2),
        (x ** 2 + (y - d) ** 2, 3)
    ]
    return min(dist)[1]


if __name__ == '__main__':
    assert get_nearest_point(5, 1, 1) == 0
    assert get_nearest_point(3, -1, -1) == 1
    assert get_nearest_point(4, 4, 4) == 2
    assert get_nearest_point(4, 2, 2) == 0
