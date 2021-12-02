data = [int(d) for d in open("input.txt").read().split("\n")]

increase = 0
for i in range(3, len(data)):
    if sum(data[i - 3:i]) < sum(data[i - 2:i+1]):
        increase += 1

print(increase)