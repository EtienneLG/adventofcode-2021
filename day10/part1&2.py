data = open("input.txt").read().split("\n")

def from_values(d, look):
    for k, v in d.items():
        if v == look:
            return k

syntax = {")": "(", "]": "[", "}": "{", ">": "<"}
illegal = {")": 3, "]": 57, "}": 1197, ">": 25137}

total_1 = 0
total_2 = []
for line in data:
    errors = 0
    chunks = []
    for c in line:
        if c in syntax.values(): chunks.append(c)
        else:
            if chunks[-1] == syntax[c]: chunks.pop(-1)
            else: errors += illegal[c] ; break
    if errors != 0: total_1 += errors
    else:
        t = 0
        for i in reversed([from_values(syntax, c) for c in chunks]):
            t = t * 5 + list(syntax.keys()).index(i) + 1
        total_2.append(t)

print(total_1, sorted(total_2)[len(total_2) // 2])
