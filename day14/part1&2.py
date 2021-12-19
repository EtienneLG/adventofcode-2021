import numpy as np

data = open("input.txt").read().split("\n\n")

polymer = data[0]
rules = dict([(a[0], a[1]) for a in [b.split(" -> ") for b in data[1].split("\n")]])
combination = {polymer[p - 1:p + 1]: 0 for p in range(1, len(polymer))}

for p in range(1, len(polymer)): combination[polymer[p - 1:p + 1]] += 1
move = {a: 0 for a in list(set(rules.values()))}
for p in polymer: move[p] = polymer.count(p)
for s in range(40):
    if s == 10: print(max(move.values()) - min(move.values()))
    new_combination = combination.copy()
    next_move = move.copy()
    for pair in combination.keys():
        if combination[pair] == 0: continue
        next_move[rules[pair]] += combination[pair]
        for p in (pair[0] + rules[pair], rules[pair] + pair[1]):
            try:
                new_combination[p] += combination[pair]
            except:
                new_combination[p] = combination[pair]
        new_combination[pair] -= combination[pair]
    combination = new_combination.copy()
    move = next_move.copy()

print(max(move.values()) - min(move.values()))