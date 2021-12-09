import numpy as np

grid = np.array([np.array([int(x) for x in str(g)]) for g in open("input.txt").read().split("\n")])

def basin_seeking(pos):
    basin_size = []
    queue = [pos]
    while len(queue) != 0:
        c = queue.pop(-1)
        basin_size += [c] if c not in basin_size else []
        poss = []
        if c[0] >= 1:
            if grid[c[0] - 1, c[1]] >= current and grid[c[0] - 1, c[1]] != 9: poss.append([c[0] - 1, c[1]])
        if c[1] < len(grid[i]) - 1:
            if grid[c[0], c[1] + 1] >= current and grid[c[0], c[1] + 1] != 9: poss.append([c[0], c[1] + 1])
        if c[0] < len(grid) - 1:
            if grid[c[0] + 1, c[1]] >= current and grid[c[0] + 1, c[1]] != 9: poss.append([c[0] + 1, c[1]])
        if c[1] >= 1:
            if grid[c[0], c[1] - 1] >= current and grid[c[0], c[1] - 1] != 9: poss.append([c[0], c[1] - 1])
        queue += [a for a in poss if a not in queue and a not in basin_size]
    return len(basin_size)

basins = []
low_points = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        current = grid[i, j]
        if i >= 1:
            if grid[i - 1, j] <= current: continue
        if j < len(grid[i]) - 1:
            if grid[i, j + 1] <= current: continue
        if i < len(grid) - 1:
            if grid[i + 1, j] <= current: continue
        if j >= 1:
            if grid[i, j - 1] <= current: continue
        low_points.append(current + 1)
        basins.append(basin_seeking([i, j]))

largest = sorted(basins)[-3:]
print(sum(low_points))
print(np.multiply.reduce(largest))
