from DefaultGenerator.default_generator import DefaultGenerator

seq1 = [4, 5, 0, 0]
seq2 = [1, 2, 3, 4]
seq3 = [4, 3, 3, 4]

default_generator = DefaultGenerator(seq2)

for i in range(10):
    x = default_generator.generate()
    print(x, end="   ")

print()
