class RLEZip:
    def __init__(self, strq):
        self.strq = strq

    @staticmethod
    def pack_l(s, cnt):
        if cnt > 1:
            return s + str(cnt)
        return s

    def rle(self):
        last_sym = self.strq[0]
        last_pos = 0
        answer = []

        for i in range(len(self.strq)):
            if self.strq[i] != last_sym:
                answer.append(self.pack_l(last_sym, i - last_pos))
                last_pos = i
                last_sym = self.strq[i]

        answer.append(self.pack_l(self.strq[last_pos],
                                  len(self.strq) - last_pos)
                      )
        return "".join(answer)


if __name__ == '__main__':
    assert RLEZip('RRRRWWLLSL').rle() == 'R4W2L2SL'
    assert RLEZip('XYZ').rle() == 'XYZ'
    assert RLEZip('X0Y0Z0').rle() == 'X0Y0Z0'
    assert RLEZip('B' * 50).rle() == 'B50'
