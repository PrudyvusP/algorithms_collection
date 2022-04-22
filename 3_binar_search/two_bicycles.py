def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l


def checkisge(index, params):
    seq, x = params
    return seq[index] >= x


def findfirstge(seq, x):
    ans = lbinsearch(0, len(seq) - 1, checkisge, (seq, x))
    if seq[ans] < x:
        return -1
    return ans + 1


if __name__ == '__main__':
    _ = input()
    seq = list(map(int, input().split()))
    x = int(input())
    first = findfirstge(seq, x)

    if first != -1:
        second = findfirstge(seq[first:len(seq)], 2 * x)
        if second == -1:
            print(first, -1)
        else:
            print(first, first + second)
    else:
        print('-1 -1')
