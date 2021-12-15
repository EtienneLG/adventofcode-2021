import numpy as np

data = open("input.txt").read().split("\n\n")
dots = np.array([[int(a) for a in b.split(",")] for b in data[0].split("\n")])

grid = np.full(shape=(dots[:, 1].max()+1,dots[:, 0].max()+1), fill_value=0)
for d in dots: grid[d[1], d[0]] = 1

for f in data[1].split("\n"):
    if data[1].split("\n").index(f) == 1: print(np.count_nonzero(grid > 0))
    way = f.split("=")[0][-1]
    how_much = int(f.split("=")[1])
    if way == "y":
        a = grid[:how_much]
        b = np.flip(grid[how_much+1:], axis=0)
        m = a.shape[0] if a.shape[0] > b.shape[0] else b.shape[0]
        a = np.append(a, np.full(shape=(m - a.shape[0], grid.shape[1]), fill_value=0), axis=0)
        b = np.append(b, np.full(shape=(m - b.shape[0], grid.shape[1]), fill_value=0), axis=0)
        grid = a + b
    elif way == "x":
        a = grid[:, :how_much]
        b = np.flip(grid[:, how_much+1:], axis=1)
        m = a.shape[1] if a.shape[1] > b.shape[1] else b.shape[1]
        a = np.append(np.full(shape=(grid.shape[0], m - a.shape[1]), fill_value=0), a, axis=1)
        b = np.append(np.full(shape=(grid.shape[0], m - b.shape[1]), fill_value=0), b, axis=1)
        grid = a + b

print(np.where(grid>0, "#", np.where(grid==0, " ", grid)))