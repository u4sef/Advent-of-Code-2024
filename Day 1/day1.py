# Read input from file
with open('day1.txt') as f:
    # 'left' and 'right' represent the two lists of numbers from the input file.
    # Each line in the file contains two numbers: the first goes into 'left' and the second into 'right'.
    left, right = zip(*(map(int, line.split()) for line in f))

# Part 1: Total distance
# 'part1' calculates the sum of absolute differences between corresponding elements of the sorted 'left' and 'right' lists.
part1 = sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))

# Part 2: Similarity score
from collections import Counter
# 'right_count' is basically a dictionary (Counter) that counts occurrences of each number in the 'right' list.
right_count = Counter(right)
# 'part2' computes the similarity score by summing, for each number in 'left', the product of the number and its count in 'right'.
part2 = sum(n * right_count[n] for n in left)


print("Part 1:", part1)
print("Part 2:", part2)