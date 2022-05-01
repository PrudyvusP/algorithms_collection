def solution(weights, colors):
    weights = list(map(int, weights.split()))
    colors = colors.split()
    d = {}
    for i in range(len(weights)):
        d[colors[i]] = d.get(colors[i], []) + [weights[i]]
    return max([i[-1] - i[0] for i in d.values()])


if __name__ == '__main__':
    print(solution(input(), input()))
