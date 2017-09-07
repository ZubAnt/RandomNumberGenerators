from DefaultGenerator.default_generator import DefaultGenerator

seq1 = [4, 5, 0, 0]
seq2 = [1, 2, 3, 4, 5, 6, 7, 8]
seq3 = [4, 3, 3, 4]

default_generator = DefaultGenerator(seq2)
x_list = list()

for i in range(1000):
    x = default_generator.generate()
    x_list.append(x)
    print("x =", x)

m = sum(x_list) / len(x_list)
print("\nm =", m)
