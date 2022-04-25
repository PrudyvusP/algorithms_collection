def get_freq_a(filename: str) -> dict:
    with open(filename, 'r') as f:
        rofel = {}
        for k in f:
            k = k.split()
            for p in k:
                rofel[p] = rofel.get(p, 0) + 1
    return rofel


def repr_res(seq: dict) -> None:
    new_seq = [(v, k) for (k, v) in seq.items()]
    new_seq.sort(key=lambda x: (-int(x[0]), x[1]))
    for k in new_seq:
        print(k[1])


repr_res(get_freq_a('input.txt'))
