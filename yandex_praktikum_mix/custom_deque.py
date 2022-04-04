# ID 66766518

ERROR_TEXT = "error"


class UnknownCommandError(Exception):
    pass


class DequeOverFlowError(Exception):
    pass


class PoppingFromEmptyDequeError(Exception):
    pass


class Deque:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size >= self.max_size

    def push_back(self, value):
        if self.is_full():
            raise DequeOverFlowError
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def push_front(self, value):
        if self.is_full():
            raise DequeOverFlowError
        self.queue[self.head - 1] = value
        self.head = (self.head - 1) % self.max_size
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            raise PoppingFromEmptyDequeError
        x = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return x

    def pop_front(self):
        if self.is_empty():
            raise PoppingFromEmptyDequeError
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return x

    def __len__(self):
        return self.size


if __name__ == '__main__':
    n, max_size = int(input()), int(input())
    deque = Deque(max_size)
    for i in range(n):
        strq = input().split()
        command = strq[0]
        if command == "push_front":
            try:
                deque.push_front(strq[1])
            except DequeOverFlowError:
                print(ERROR_TEXT)
        elif command == "push_back":
            try:
                deque.push_back(strq[1])
            except DequeOverFlowError:
                print(ERROR_TEXT)
        elif command == "pop_front":
            try:
                print(deque.pop_front())
            except PoppingFromEmptyDequeError:
                print(ERROR_TEXT)
        elif command == "pop_back":
            try:
                print(deque.pop_back())
            except PoppingFromEmptyDequeError:
                print(ERROR_TEXT)
        else:
            raise UnknownCommandError
