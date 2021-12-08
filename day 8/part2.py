data = [d.split(" | ") for d in open("input.txt").read().split("\n")]

numbs = {"012456":0, "25":1, "02346":2, "02356":3, "1235":4, "01356":5, "013456":6, "025":7, "0123456":8, "012356":9}

def all_poss(p):
    a = []
    for i in p[1]:
        for j in p[2]:
            for k in p[4]:
                for l in p[4]:
                    a.append(sorted(p[0][0] + i + j + k + l))
    return a

def find_pattern(pattern):
    possibilities = dict((a, []) for a in range(7))

    one = next(p for p in pattern if len(p) == 2)
    possibilities[2] = list(one)
    possibilities[5] = list(one)

    seven = next(p for p in pattern if len(p) == 3)
    possibilities[0] = list(set(seven) - (set(one)))

    four = next(p for p in pattern if len(p) == 4)
    possibilities[1] = list(set(four) - (set(one + seven)))
    possibilities[3] = list(set(four) - (set(one + seven)))

    possibilities[4] = list(set("abcdefg") - (set(one + seven + four)))
    possibilities[6] = list(set("abcdefg") - (set(one + seven + four)))

    possible_two = all_poss(possibilities)
    two = next(p for p in pattern if sorted(p) in possible_two)
    possibilities[2] = list(set(two) & (set(possibilities[2])))
    possibilities[5] = list(set(possibilities[5]) - (set(possibilities[2])))
    possibilities[3] = list(set(two) & (set(possibilities[3])))
    possibilities[1] = list(set(possibilities[1]) - (set(possibilities[3])))

    nine = next(p for p in pattern if len(p) == 6 and len(list(set(p) - set(one + four + seven))) == 1)
    possibilities[6] = list(set(nine) - set(one + four + seven))
    possibilities[4] = list(set(possibilities[4]) - (set(possibilities[6])))

    return dict((j[0], str(i)) for i, j in possibilities.items())

patterns = dict((d[0], d[1]) for d in data)

total_codes = []
for p, c in patterns.items():
    pattern = find_pattern(p.split(" "))
    code = []
    for i in c.split(" "):
        code.append(numbs["".join(sorted("".join([pattern[m] for m in list(i)])))])
    total_codes.append(int("".join([str(c) for c in code])))

print(sum(total_codes))