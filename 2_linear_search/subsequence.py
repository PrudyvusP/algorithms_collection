def is_subsequence(s, t):
    start = -1
    for i in s:
        start = t.find(i, start + 1)
        if start == -1:
            return False
    return True


a, b = input(), input()
print(is_subsequence(a, b))
