import numpy as np

data = np.array(open("input.txt").read().split("\n"))

gamma = ""
epsilon = ""

for i in range(len(data[0])):
    new_digit = 1 if np.sum(np.vectorize(lambda x: int(x[i]))(data)) > len(data) / 2 else 0
    gamma += str(new_digit)
    epsilon += str((new_digit + 1) % 2)

print(int(gamma, 2) * int(epsilon, 2))