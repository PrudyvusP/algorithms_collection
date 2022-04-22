def is_first_card_weaker(a, b):
    a_len = len(a)
    b_len = len(b)
    if a_len == b_len:
        len_f = a_len
    else:
        len_f = a_len + b_len

    for i in range(0, len_f):
        if i < a_len:
            char_ac = a[i]
        else:
            char_ac = b[i - a_len]
        if i < b_len:
            char_bc = b[i]
        else:
            char_bc = a[i - b_len]
        if char_bc == char_ac:
            continue
        if char_ac < char_bc:
            return False
        return True


def insertion_sort_by_comparator(array, key_func):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and key_func(item_to_insert, array[j - 1]):
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert


"""
    private int compare(String a, String b) {
        int a_len = a.length();
        int b_len = b.length();
        int len = a_len == b_len ? a_len : a_len + b_len;
        for (int i=0; i < len; i++) {
            char ac = i < a_len ? a.charAt(i) : b.charAt(i-a_len);
            char bc = i < b_len ? b.charAt(i) : a.charAt(i-b_len);
            if (ac == bc) continue;
            return ac < bc ? -1 : 1;
        }
        return 0;
"""

if __name__ == '__main__':
    _ = input()
    rofel = input().split()
    insertion_sort_by_comparator(rofel, is_first_card_weaker)
    print(*rofel, sep='')
