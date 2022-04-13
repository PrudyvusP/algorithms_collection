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

"""
q = Queue(8)
q.push(1)
print(q.queue)  # [1, None, None, None, None, None, None, None]
print(q.size)   # 1
q.push(-1)
q.push(0)
q.push(11)
print(q.queue)  # [1, -1, 0, 11, None, None, None, None]
print(q.size)   # 4

q.pop()
print(q.queue)  # [None, -1, 0, 11, None, None, None, None]
print(q.size)   # 3


q.pop()
q.pop()
q.push(-8)
q.push(7)
q.push(3)
q.push(16)
print(q.queue) # [None, None, None, 11, -8, 7, 3, 16]
print(q.size) # 5
q.push(12)
print(q.queue) # [12, None, None, 11, -8, 7, 3, 16]
print(q.size) # 6
"""
