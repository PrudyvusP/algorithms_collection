def two_sum(seq, x):
    prev_nums_seq = set()
    for item in seq:
        if x - item in prev_nums_seq:
            return item, x - item
        prev_nums_seq.add(item)
    return 0, 0


"""
Дана последовательность положительных чисел длиной N и число X
Нужно найти два различных числа A и B из последовательности, таких что A + B = X или вернуть 0, 0, если такой пары чисел нет
"""