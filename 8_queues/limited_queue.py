class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_n = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def peek(self):
        return self.queue[self.head] if not self.is_empty() else None

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print("error")

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x


if __name__ == '__main__':
    _, max_size = int(input()), int(input())
    queue = MyQueueSized(max_size)
    for i in range(_):
        strq = input().split()
        if strq[0] == "push":
            queue.push(int(strq[1]))
        elif strq[0] == "peek":
            print(queue.peek())
        elif strq[0] == "size":
            print(queue.size)
        else:
            print(queue.pop())
