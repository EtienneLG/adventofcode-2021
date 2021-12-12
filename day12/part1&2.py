caves = {}

def plus_one(a, b):
    try:
        caves[a] += [b]
    except:
        caves[a] = [b]

for c in open("input.txt").read().split("\n"):
    a = c.split("-")
    plus_one(a[0], a[1])
    plus_one(a[1], a[0])

p = set()
def paths(current, last):
    if current == "end": p.add(",".join(last)) ; return -1
    for c in caves[current]:
        if c == twice and last.count(c) != 2: paths(c, last + [c])
        if c.islower() and c in last: continue
        else: paths(c, last + [c])

for i in caves.keys():
    if i.islower() and i not in ("start", "end"):
        twice = i
        paths("start", ["start"])
print(len(p))