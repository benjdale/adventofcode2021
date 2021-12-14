depth_increases = 0

with open("../data/day1.txt") as file:
    lines = [int(line.strip()) for line in file]
    for index, line in enumerate(lines):
        if line > lines[index - 1]:
            depth_increases += 1

print(f"{depth_increases} depth increases")
