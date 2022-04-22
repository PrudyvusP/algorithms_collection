def isSubsequence(s, t):
    start = -1
    for i in s:
        start = t.find(i, start + 1)
        if start == -1:
            return False
    return True

a, b = input(), input()
print(isSubsequence(a, b))
