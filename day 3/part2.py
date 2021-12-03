import numpy as np

data = np.array(open("input.txt").read().split("\n"))

oxygen_indices = data
co2_indices = data
for i in range(len(data[0])):
    if len(oxygen_indices) != 1:
        row = np.vectorize(lambda x: int(x[i]))(oxygen_indices)
        oxy_most = 1 if sum(row) >= (len(row) / 2) else 0
        oxygen_indices = oxygen_indices[np.where(row == oxy_most)]
    if len(co2_indices) != 1:
        row = np.vectorize(lambda x: int(x[i]))(co2_indices)
        co2_most = 0 if sum(row) >= (len(row) / 2) else 1
        co2_indices = co2_indices[np.where(row == co2_most)]
    if len(oxygen_indices) == 1 and len(co2_indices) == 1:
        print(int(oxygen_indices[0], 2) * int(co2_indices[0], 2))
        break