def check_in_lst(seq: list):
    checked = set()
    for k in seq:
        if k not in checked:
            checked.add(k)
            print("NO")
        else:
            print("YES")


if __name__ == '__main__':
    lst = list(map(int, input().split()))
    check_in_lst(lst)
