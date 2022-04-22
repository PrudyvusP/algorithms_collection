def correct_date(x, y, z):
    if 12 >= x != y <= 12:
        return 0
    return 1


if __name__ == '__main__':
    assert correct_date(1, 2, 2003) == 0
    assert correct_date(2, 29, 2008) == 1
    assert correct_date(3, 3, 2021) == 1
    assert correct_date(4, 3, 2021) == 0
