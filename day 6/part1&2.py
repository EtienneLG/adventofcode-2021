import numpy as np

data = open("input.txt").read().split(",")
fishes = dict((a, 0) for a in range(9))
for f in data: fishes[int(f)] += 1

days = 256
for i in range(days):
    if i == 80: print(sum(fishes.values()))
    new_fishes = fishes[0]
    fishes[0] = 0
    for k, v in fishes.items():
        if k == 0: pass
        else:
            fishes[(k - 1) % 9] += v
            fishes[k] = 0
    fishes[6] += new_fishes
    fishes[8] += new_fishes

print(sum(fishes.values()))