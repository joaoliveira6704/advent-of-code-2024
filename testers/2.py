list1 = []

with open(".\\testers\\data2.csv", "r") as f:
    lines = f.readlines()

for line in lines:
    fields = line.strip().split(";")
    report = [int(field) for field in fields]
    list1.append(report)

safeTotal = 0
unsafeTotal = 0

def is_increasing(levels):
    return all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))

def is_decreasing(levels):
    return all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))

def has_valid_diff(levels):
    return all(1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1))

for i, levels in enumerate(list1):
    if (is_increasing(levels) or is_decreasing(levels)) and has_valid_diff(levels):
        safeTotal += 1
        print(f"line {i + 1} safe")
    else:
        unsafeTotal += 1
        print(f"line {i + 1} unsafe")

print(f"Safe: {safeTotal}\nUnsafe: {unsafeTotal}")