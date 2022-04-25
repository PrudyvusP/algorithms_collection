def count_guys(filename):
    with open(filename, 'r') as f:
        rofel = {}
        for k in f:
            k = k.strip().split()
            rofel[k[0]] = rofel.get(k[0], 0) + int(k[1])
    for k in sorted(rofel):
        print(k, rofel[k])


count_guys('input.txt')
