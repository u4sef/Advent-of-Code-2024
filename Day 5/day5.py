# Read the input file and split it into rules and updates sections
with open('day5.txt', 'r') as f:
    sections = f.read().split('\n\n')

# Parse the rules as tuples of integers and updates as lists of integers
rules = [tuple(map(int, line.split('|'))) for line in sections[0].strip().split('\n')]
updates = [list(map(int, line.split(','))) for line in sections[1].strip().split('\n')]

part1 = part2 = 0
for update in updates:
    # Check if the update is correctly ordered according to the rules
    if all(update.index(x) < update.index(y) for x, y in rules if x in update and y in update):
        # Add the middle element of the correctly ordered update to part1
        part1 += update[len(update) // 2]
    else:
        # Create a dependency graph for the pages in the update
        graph = {page: [] for page in update}
        for x, y in rules:
            if x in update and y in update:
                graph[y].append(x)
        sorted_update = []
        # Topological sort to resolve the correct order
        while graph:
            no_deps = [page for page, deps in graph.items() if not deps]
            if not no_deps:
                raise ValueError("Circular dependency detected.")
            sorted_update.extend(no_deps)
            graph = {p: [d for d in deps if d not in no_deps] for p, deps in graph.items() if p not in no_deps}
        # Add the middle element of the sorted update to part2
        part2 += sorted_update[len(sorted_update) // 2]

# Print results for both parts
print("Part 1:", part1)
print("Part 2:", part2)
