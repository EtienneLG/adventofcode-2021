data = [d.split(" ") for d in open("input.txt").read().split("\n")]

pos = {"position": 0, "depth": 0, "aim": 0}

for i in data:
  if i[0] == "forward":
    pos["position"] += int(i[1])
    pos["depth"] += pos["aim"] * int(i[1])
  elif i[0] == "down":
    pos["aim"] += int(i[1])
  elif i[0] == "up":
    pos["aim"] -= int(i[1])

print(pos["position"] * pos["depth"])