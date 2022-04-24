def solution(file_name):
    with open(file_name) as f:
        maxi = int(f.readline())
        data = set(range(1, maxi + 1))
        rofel = set()
        for i in f:
            if i.strip().replace(' ', '').isdigit():
                strq = set(map(int, i.split()))
            elif i.strip() == 'YES':
                data = data.intersection(strq)
            elif i.strip() == 'NO':
                for k in strq:
                    rofel.add(k)
        print(*sorted(data.difference(rofel)))


if __name__ == '__main__':
    solution('input.txt')
