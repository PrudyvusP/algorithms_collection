# ID 66731453

class Deque:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, value):
        if self.size != self.max_size:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            return "error"

    def push_front(self, value):
        if self.size != self.max_size:
            self.queue[self.head - 1] = value
            self.head = (self.head - 1) % self.max_size
            self.size += 1
        else:
            return "error"

    def pop_back(self):
        if self.is_empty():
            return "error"

        x = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return x

    def pop_front(self):
        if self.is_empty():
            return "error"

        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return x


if __name__ == '__main__':
    n, max_size = int(input()), int(input())
    deque = Deque(max_size)
    for i in range(n):
        strq = input().split()
        if strq[0].startswith("push_f"):
            result = deque.push_front(strq[1])
            if result:
                print(result)
        elif strq[0].startswith("push_b"):
            result = deque.push_back(strq[1])
            if result:
                print(result)
        elif strq[0].startswith("pop_f"):
            print(deque.pop_front())
        else:
            print(deque.pop_back())
