def count_colors(pairs: list) -> dict:
    rofel = {}
    for k in pairs:
        rofel[k[0]] = rofel.get(k[0], 0) + int(k[1])
    return rofel


def print_stdout(seq: dict) -> None:
    for k in sorted(seq):
        print(k, seq[k])


n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]
print_stdout(count_colors(data))
