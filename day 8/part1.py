data = [d.split(" | ")[-1] for d in open("input.txt").read().split("\n")]

total = 0
for i in data:
    for el in i.split(" "):
        if len(el) in (2, 3, 4, 7): total += 1

print(total)