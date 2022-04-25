def is_palindrom(strq: str) -> bool:
    i = 0
    j = len(strq) - 1
    while i < j:
        if not strq[i].isalnum():
            i += 1
            continue
        if not strq[j].isalnum():
            j -= 1
            continue
        if strq[i].lower() != strq[j].lower():
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    strq = input()
    print(is_palindrom(strq))
