from default.generator import DefaultGenerator
from congruent.generator import CongruentGenerator
import numpy as np

seq1 = [4, 5, 0, 0]
seq2 = [1, 2, 3, 4, 5, 6, 7, 8]
seq3 = [4, 3, 3, 4]
seq4 = [3, 9, 0, 6, 2, 5, 0, 0]

m = 24
lamb = 123456789
z0 = 11111111
nu = 0


# m = 4
# lamb = 2
# z0 = 11
# nu = 5

# m = 4
# lamb = 5
# z0 = 7
# nu = 0

default_generator = DefaultGenerator(seq2)
congruent_generator = CongruentGenerator(m, lamb, z0, nu)

default_list = list()
congruent_list = list()

for i in range(10000):
    # default_val = default_generator.generate()
    # print("default_val =", default_val, end="; ")
    # default_list.append(default_val)

    congruent_val = congruent_generator.generate()
    congruent_list.append(congruent_val)
    print("congruent_val =", congruent_val)

# m_default = sum(default_list) / len(default_list)
m_congruent = sum(congruent_list) / len(congruent_list)

# print("\nm_default =", m_default)
print("\nm_congruent =", m_congruent)

