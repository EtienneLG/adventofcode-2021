import numpy as np
import re

data = [re.findall("(\d+),(\d+) -> (\d+),(\d+)", d) for d in open("input.txt").read().split("\n")]
entries = np.array([((int(d[0][0]), int(d[0][1])), (int(d[0][2]), int(d[0][3]))) for d in data])
grid_size = np.max(entries.flatten()) + 1
diagram = np.array([[0 for e in range(grid_size)] for f in range(grid_size)])

for e in entries:
    if e[0][1] == e[1][1]:
        start = min(e[0][0], e[1][0])
        end = max(e[0][0], e[1][0]) + 1
        for i in range(start, end):
            diagram[e[0][1], i] = 1 if diagram[e[0][1], i] == 0 else 2
    elif e[0][0] == e[1][0]:
        start = min(e[0][1], e[1][1])
        end = max(e[0][1], e[1][1]) + 1
        for i in range(start, end):
            diagram[i, e[0][0]] = 1 if diagram[i, e[0][0]] == 0 else 2

print(np.count_nonzero(diagram.flatten() == 2))
