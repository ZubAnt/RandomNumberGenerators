import numpy as np


class CongruentGenerator(object):

    def __init__(self, mu: int, lamb: int, z0: int):
        self._mu = mu
        self._lamb = lamb
        self._z0 = z0
        self._divider = 2 ** mu

    # @property
    # def mu(self) -> int:
    #     return self._mu
    #
    # @property
    # def lamb(self) -> int:
    #     return self._lamb
    #
    # @property
    # def z0(self) -> int:
    #     return self._z0

    def generate(self):
        zlamb = self._z0 * self._lamb
        zlamb_binary = np.binary_repr(zlamb, width=self._mu)
        z1_binary =  zlamb_binary[len(zlamb_binary) - self._mu:]
        self._z0 = int(z1_binary, base=2)
        return self._z0 / self._divider


