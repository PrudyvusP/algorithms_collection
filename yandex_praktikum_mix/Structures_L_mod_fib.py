n, k = map(int, input().split())


def fib(n):
    f0, f1 = 1, 1
    for i in range(n - 1):
        f0, f1 = f1, (f0 + f1) % (pow(10, k))
    return f1


if __name__ == "__main__":
    print(fib(n))
