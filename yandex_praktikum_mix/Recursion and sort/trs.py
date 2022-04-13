def gen_binary(n, prefix):
    if n == 0:
        print(prefix)
    else:
        gen_binary(n - 1, prefix + '(')
        gen_binary(n - 1, prefix + ')')

if __name__ == '__main__':
    gen_binary(3, '()')