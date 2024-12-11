# Read input from file
with open('day9.txt') as f:
    # 'disk_map' represents the dense format of the disk layout from the input file.
    disk_map = f.read().strip()

# Parse the disk map
# 'blocks' is the expanded list representing files and free spaces based on the input format.
blocks = []
for i, length in enumerate(map(int, disk_map)):
    blocks.extend([i // 2 if i % 2 == 0 else '.' for _ in range(length)])

# Part 1: Move blocks one at a time
# 'compact_blocks' represents the state of the disk after compacting blocks one by one.
compact_blocks = blocks[:]
for i in range(len(compact_blocks) - 1, -1, -1):
    if compact_blocks[i] != '.':
        j = i
        while j > 0 and compact_blocks[j - 1] == '.':
            compact_blocks[j - 1], compact_blocks[j] = compact_blocks[j], '.'
            j -= 1

# Calculate the checksum for Part 1
# 'part1' computes the checksum by summing position * file ID for each block.
part1 = sum(pos * int(block) for pos, block in enumerate(compact_blocks) if block != '.')

# Part 2: Move whole files
# 'compact_files' represents the state of the disk after compacting files as whole units.
compact_files = blocks[:]
for file_id in sorted(set(compact_files) - {'.'}, reverse=True):
    file_blocks = [i for i, block in enumerate(compact_files) if block == file_id]
    if not file_blocks:
        continue
    file_size = len(file_blocks)
    for i in range(len(compact_files)):
        if compact_files[i:i + file_size] == ['.'] * file_size:
            compact_files[i:i + file_size] = [file_id] * file_size
            for j in file_blocks:
                compact_files[j] = '.'
            break

# Calculate the checksum for Part 2
# 'part2' computes the checksum by summing position * file ID for each block.
part2 = sum(pos * int(block) for pos, block in enumerate(compact_files) if block != '.')

print("Part 1:", part1)
print("Part 2:", part2)
