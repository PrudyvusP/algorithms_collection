def min_dist(n, i, j):
    dist1 = abs(j - i) - 1
    dist2 = n - 2 - dist1
    return min(dist1, dist2)


if __name__ == '__main__':
    assert min_dist(100, 5, 6) == 0
    assert min_dist(10, 1, 9) == 1
