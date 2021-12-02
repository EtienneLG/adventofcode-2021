data = [d.split(" ") for d in open("input.txt").read().split("\n")]

pos = [0, 0]

for i in data:
  if i[0] == "forward":
    pos[0] += int(i[1])
  elif i[0] == "down":
    pos[1] += int(i[1])
  elif i[0] == "up":
    pos[1] -= int(i[1])

print(pos[0] * pos[1])