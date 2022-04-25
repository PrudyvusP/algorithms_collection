def do_smth(filename: str) -> tuple:
    with open(filename, 'r') as f:
        rofel = []
        count = 0
        party_counter = 0
        for k in f:
            k = k.split()
            rofel.append([" ".join(k[:-1]), int(k[-1]), party_counter])
            party_counter += 1
            count += int(k[-1])
    return rofel, count


def get_first_izb(_total: int) -> float:
    _n = 450
    return _total / _n


def get_votes(data: list, udel: float):
    sum = 0
    for party in data:
        party.extend([int(party[1] // udel), party[1] % udel])
        sum += party[3]
    data.sort(key=lambda x: (-x[4], x[1]))
    for i in range(450 - sum):
        data[i][3] += 1
    return data


if __name__ == '__main__':
    data = do_smth('input.txt')
    first = get_first_izb(data[1])
    new_data = get_votes(data[0], first)
    new_data.sort(key=lambda x: x[2])
    for data in new_data:
        print(data[0], data[3])
