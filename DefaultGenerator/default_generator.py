from DefaultGenerator.sequence import Sequence


class DefaultGenerator(object):

    def __init__(self, sequence):
        self._sequence = Sequence(sequence)
        self._init_number = self._sequence.toNumber()
        self._x = self._init_number

    @property
    def x(self):
        return self._x

    @property
    def init_number(self):
        return self._init_number

    @property
    def sequence(self):
        return self._sequence

    def generate(self):
        new_x = self._x ** 2
        new_x_str = "{{:.{}f}}".format(2 * self.sequence.size).format(new_x)
        sub_sequence_str = new_x_str[self.sequence.size: 2 * self.sequence.size]

        # print(sub_sequence_str)

        self._x = Sequence([int(i) for i in sub_sequence_str]).toNumber()

        return self.x
