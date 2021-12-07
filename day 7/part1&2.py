data = sorted([int(d) for d in open("input.txt").read().split(",")])

def median(arr):
    mid = len(arr) / 2
    if type(mid) == float: return arr[int(mid)]
    else: return (arr[mid] + arr[mid + 1]) / 2

m = median(data)

fuel_1 = 0
fuel_2 = 9999*99999

for i in range(data[-1]):
    fuel = 0
    for pos in data:
        fuel += sum(list(range(max(pos, i) + 1 - min(pos, i))))
    if fuel < fuel_2:
        fuel_2 = fuel
    if fuel > fuel_2: break

print(sum([abs(i - m) for i in data]))
print(fuel_2)