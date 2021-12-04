import numpy as np
import re

def from_values(d, look):
    for k, v in d.items():
        if v == look:
            return k

data = open("input.txt").read().split("\n\n")

draw = list(map(int, data[0].split(",")))
order = dict((d, draw.index(d)) for d in draw)
vector = np.vectorize(lambda x: order[x])
boards = np.array([np.array([vector(np.array(re.findall("\s*(\d*)\s*", data[b+1].split("\n")[r])[:-1], dtype="int32")) for r in range(5)]) for b in range(len(data[1:]))])

maximums = [1000 for i in range(len(boards))]

for b in range(len(boards)):
    for l in boards[b]:
        if np.max(l) < maximums[b]:
            maximums[b] = np.max(l)
    rows = np.transpose(boards[b])
    for r in rows:
        if np.max(r) < maximums[b]:
            maximums[b] = np.max(r)

def score(last):
    winning_board = maximums.index(last)
    unmarked = boards[winning_board].flatten()
    return sum(np.vectorize(lambda x: from_values(order, x)) (unmarked[unmarked > last])) * from_values(order, last)

print(score(min(maximums)), score(max(maximums)))