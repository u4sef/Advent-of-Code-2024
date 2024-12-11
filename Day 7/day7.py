# Read input from file
with open('day7.txt') as f:
    # 'equations' is a list of tuples where each tuple contains the target value (test_value)
    # and a list of numbers (values) from the input file.
    equations = [(int(line.split(':')[0]), list(map(int, line.split(':')[1].split()))) for line in f]

# Helper function to evaluate an expression left-to-right with custom operators
def evaluate(numbers, operators):
    # 'res' starts with the first number and applies the operators sequentially
    res = numbers[0]
    for num, op in zip(numbers[1:], operators):
        # Perform addition, multiplication, or concatenation based on 'op'
        res = res + num if op == '+' else res * num if op == '*' else int(str(res) + str(num))
    return res

# Part 1: Solve using only addition (+) and multiplication (*)
from itertools import product
# 'part1' calculates the sum of test values that can be made valid using only + and *
part1 = sum(test for test, nums in equations if any(
    evaluate(nums, ops) == test for ops in product(['+', '*'], repeat=len(nums) - 1)
))

# Part 2: Solve using addition (+), multiplication (*), and concatenation (||)
# 'part2' calculates the sum of test values that can be made valid using +, *, and ||
part2 = sum(test for test, nums in equations if any(
    evaluate(nums, ops) == test for ops in product(['+', '*', '||'], repeat=len(nums) - 1)
))

print("Part 1:", part1)
print("Part 2:", part2)
