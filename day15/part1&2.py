from heapq import heappop, heappush


def expand_map(risks):
    height = len(risks)
    width = len(risks[0])
    expanded = []

    for row in range(height * 5):
        expanded_row = []
        for column in range(width * 5):
            risk = (risks[row % height][column % width] + row // height + column // width - 1) % 9 + 1
            expanded_row.append(risk)
        expanded.append(expanded_row)

    return expanded


def lowest_total_risk(risks):
    height = len(risks)
    width = len(risks[0])
    start, end = (0, 0), (height - 1, width - 1)
    distances = [[float("inf")] * width for _ in range(height)]
    distances[0][0] = 0
    queue = [(0, start)]
    destinations = ((-1, 0), (0, 1), (1, 0), (0, -1))

    while queue:
        risk, (row, column) = heappop(queue)
        if risk != distances[row][column]:
            continue
        if (row, column) == end:
            return risk

        for row_delta, column_delta in destinations:
            next_row = row + row_delta
            next_column = column + column_delta
            if 0 <= next_row < height and 0 <= next_column < width:
                next_risk = risk + risks[next_row][next_column]
                if next_risk < distances[next_row][next_column]:
                    distances[next_row][next_column] = next_risk
                    heappush(queue, (next_risk, (next_row, next_column)))


with open("input.txt") as input_file:
    input_risks = [[int(value) for value in line.strip()] for line in input_file]

print("Part 1 total risk:", lowest_total_risk(input_risks))
print("Part 2 total risk:", lowest_total_risk(expand_map(input_risks)))
