import numpy as np

grid = np.array([np.array([int(x) for x in str(g)]) for g in open("input.txt").read().split("\n")])

increase = np.vectorize(lambda x: x + 1)
total = 0

size = len(grid)+1
for s in range(1000):
    if s == 100: print(total)
    grid = increase(grid)
    flashes = np.array(np.where(grid > 9))
    if len(flashes[0]) != 0:
        while True:
            flashes = np.array(np.where(grid > 9))
            if len(flashes[0]) == 0: break
            queue = [[flashes[0][x], flashes[1][x]] for x in range(len(flashes[0]))]
            for c in queue:
                grid[c[0], c[1]] = 0
                total += 1
                for pos in ((-1, -1),(-1, 0),(-1, 1),(0, 1),(1, 1),(1, 0),(1, -1),(0, -1)):
                    try:
                        if grid[(c[0]+pos[0])%size, (c[1]+pos[1])%size] != 0: grid[c[0] + pos[0], c[1] + pos[1]] += 1
                    except:
                        continue
    if grid.sum() == 0: print(s+1) ; break
