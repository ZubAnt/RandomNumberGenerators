import numpy as np


class CongruentGenerator(object):

    def __init__(self, m: int, lamb: int, z0: int, nu: int = 0) -> None:
        self._m = m
        self._lamb = lamb
        self._z0 = z0
        self._divider = 2 ** m
        self._nu = nu

    def generate(self) -> float:

        zlamb = self._z0 * self._lamb + self._nu
        zlamb_binary = np.binary_repr(zlamb, width=self._nu)

        z1_binary = zlamb_binary[len(zlamb_binary) - self._m:]
        self._z0 = int(z1_binary, base=2)

        # print(f'zlamb = {zlamb}; zlamb_binary = {zlamb_binary}; z1_binary = {z1_binary}; z1 = {self._z0};')

        return float(self._z0 / self._divider)


