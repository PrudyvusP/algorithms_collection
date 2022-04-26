class StackMax:
    def __init__(self):
        self.stack = []
        self.cur_maxes = []

    def push(self, x):
        if not self.cur_maxes or x > self.cur_maxes[-1]:
            self.cur_maxes.append(x)
        else:
            self.cur_maxes.append(self.cur_maxes[-1])
        self.stack.append(x)

    def pop(self):
        if not self.stack:
            return "error"
        self.stack.pop()
        self.cur_maxes.pop()

    def get_max(self):
        if not self.stack:
            return None
        return self.cur_maxes[-1]


if __name__ == '__main__':
    _ = int(input())
    stack = StackMax()
    for i in range(_):
        strq = input().split()
        if strq[0] == 'get_max':
            print(stack.get_max())
        elif strq[0] == 'push':
            stack.push(int(strq[1]))
        else:
            p = stack.pop()
            if p:
                print(p)
