from functools import reduce


class Sequence(object):

    def __init__(self, sequence):

        if len(sequence) % 2 != 0:
            sequence.append(1)

        if len(sequence) == 0:
            sequence = [1, 2]

        self._sequence = sequence
        self._length = len(sequence)

    @property
    def sequence(self):
        return self._sequence

    @property
    def length(self):
        return self._length

    @property
    def size(self):
        return self._length

    def toNumber(self):
        return float(reduce(lambda a, var: a + str(var), self._sequence, '0.'))

