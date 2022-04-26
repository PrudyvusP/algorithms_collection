from operator import add, sub, mul, floordiv

operators = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": floordiv
}

SINGLE_NUM_CONST = 2


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


def solution(strq: str) -> int:
    stack = Stack()
    items = strq.split()

    if len(items) < SINGLE_NUM_CONST:
        return int(items[0])

    for symb in items:
        if symb not in operators:
            stack.push(int(symb))
        else:
            digit2, digit1 = int(stack.pop()), int(stack.pop())
            stack.push(operators[symb](digit1, digit2))
    return stack.peek()


def test():
    assert solution('-123') == -123
    assert solution('-4 4 +') == 0
    assert solution('4 2 * 4 / 25 * 2 - 12 / 500 2 * + 2 / -999 + 71 + -1 *') == 426
    assert solution('4 2 * 4 / 25 * 2 - 12 / 500 2 * + 2 / -999 + 71 + -1 * 2 /') == 213
    assert solution('2 1 + 3 *') == 9
    assert solution('7 2 + 4 * 2 +') == 38
    assert solution('10 2 4 * -')
    assert solution('12 5 /') == 2
    assert solution('3 4 +') == 7


if __name__ == '__main__':
    print(solution(input()))
