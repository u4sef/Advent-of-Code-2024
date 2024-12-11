from collections import defaultdict

# Read input file
input_file = 'day8.txt'
data = open(input_file).read().strip()

# Initialize variables
part1_result = 0
part2_result = 0

grid = data.split('\n')
num_rows = len(grid)
num_cols = len(grid[0])
points = defaultdict(list)

# Parse grid and populate points dictionary
for row in range(num_rows):
    for col in range(num_cols):
        if grid[row][col] != '.':
            points[grid[row][col]].append((row, col))

aligned_points_part1 = set()
aligned_points_part2 = set()

# Check alignments and compute results
for row in range(num_rows):
    for col in range(num_cols):
        for key, coordinates in points.items():
            for (row1, col1) in coordinates:
                for (row2, col2) in coordinates:
                    if (row1, col1) != (row2, col2):
                        dist1 = abs(row - row1) + abs(col - col1)
                        dist2 = abs(row - row2) + abs(col - col2)

                        delta_row1 = row - row1
                        delta_row2 = row - row2
                        delta_col1 = col - col1
                        delta_col2 = col - col2

                        # Check if points are collinear
                        if (dist1 == 2 * dist2 or dist1 * 2 == dist2) and 0 <= row < num_rows and 0 <= col < num_cols and (delta_row1 * delta_col2 == delta_col1 * delta_row2):
                            aligned_points_part1.add((row, col))
                        if 0 <= row < num_rows and 0 <= col < num_cols and (delta_row1 * delta_col2 == delta_col1 * delta_row2):
                            aligned_points_part2.add((row, col))

part1_result = len(aligned_points_part1)
part2_result = len(aligned_points_part2)

# Output the results
print(part1_result)
print(part2_result)