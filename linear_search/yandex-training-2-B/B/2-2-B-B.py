def find_max_dist(seq):
    max_distance = 0
    for i in range(len(seq)):
        if seq[i] == 1:
            distances = []
            for j in range(len(seq)):
                if seq[j] == 2:
                    distances.append(abs(i - j))
            if max_distance <= min(distances):
                max_distance = min(distances)
    return max_distance


def find_max_dist_opt(seq):
    shops = -20
    left = [0] * len(seq)
    for i in range(len(seq)):
        if seq[i] == 2:
            shops = i
        if seq[i] == 1:
            left[i] = i - shops
    ans = 0
    shops = 30
    for i in range(len(seq) - 1, -1, -1):
        if seq[i] == 2:
            shops = i
        if seq[i] == 1:
            mindist = min(shops - i, left[i])
            ans = max(ans, mindist)
    return ans


if __name__ == '__main__':
    assert find_max_dist([2, 0, 1, 1, 0, 1, 0, 2, 1, 2]) == 3
    assert find_max_dist([1, 2, 0, 0, 1, 0, 2, 1, 0, 2]) == 2
    assert find_max_dist_opt([2, 0, 1, 1, 0, 1, 0, 2, 1, 2]) == 3
    assert find_max_dist_opt([1, 2, 0, 0, 1, 0, 2, 1, 0, 2]) == 2
