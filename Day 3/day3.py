import re

# Read input from file
with open('day3.txt') as f:
    memory = f.read()

# Extract and sum mul results
# This lambda function uses a regular expression(https://en.wikipedia.org/wiki/Regular_expression) to find all
# valid 'mul(X,Y)' patterns in the memory.

# It captures X and Y, converts them to integers, calculates their product, and returns the total sum.
extract_mul = lambda mem: sum(int(x) * int(y) for x, y in re.findall(r'mul\((\d+),(\d+)\)', mem))

# Part 1: Sum of all valid mul results
part1 = extract_mul(memory)

# Part 2: Sum with conditional enabling/disabling
enabled, part2 = True, 0
for segment in re.split(r'(do\(\)|don\'t\(\))', memory):
    if segment == "do()": enabled = True
    elif segment == "don't()": enabled = False
    elif enabled: part2 += extract_mul(segment)

print("Part 1:", part1)
print("Part 2:", part2)
