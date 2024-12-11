# Read input from file
with open('day2.txt') as f:
    reports = [list(map(int, line.split())) for line in f]

# Helper to check if levels are valid
# This lambda function performs two checks:
# (1) All adjacent differences in the report must be between 1 and 3 [1 <= abs(r[i] - r[i+1]) <= 3].
# (2) The levels must either strictly increase or strictly decrease throughout the report.
check = lambda r: all(1 <= abs(r[i] - r[i+1]) <= 3 for i in range(len(r) - 1)) and (
    all(r[i] < r[i+1] for i in range(len(r) - 1)) or all(r[i] > r[i+1] for i in range(len(r) - 1)))

# Part 1: Safe reports without Problem Dampener
part1 = sum(check(r) for r in reports)

# Part 2: Safe reports with Problem Dampener
part2 = sum(any(check(r[:i] + r[i+1:]) for i in range(len(r))) or check(r) for r in reports)

print("Part 1:", part1)
print("Part 2:", part2)
