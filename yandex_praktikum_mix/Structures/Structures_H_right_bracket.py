data = {
    ")": "(",
    "}": "{",
    "]": "["
}


def is_correct_bracket_seq(seq: str) -> bool:
    stack = []
    for symb in seq:
        if symb in '{[(':
            stack.append(symb)
        else:
            if not stack:
                return False
            else:
                t = stack.pop()
                if data[symb] != t:
                    return False
    return len(stack) == 0


if __name__ == '__main__':
    assert is_correct_bracket_seq('((())]') is False
    assert is_correct_bracket_seq('{[()]}') is True
    strq = input()
    print(is_correct_bracket_seq(strq))
