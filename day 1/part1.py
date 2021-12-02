data = [int(d) for d in open("input.txt").read().split("\n")]

increase = 0
for i in range(1, len(data)):
    if data[i - 1] < data[i]:
        increase += 1

print(increase)