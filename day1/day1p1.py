depth_increases = 0

with open("../data/day1.txt") as file:
    lines = [int(line.strip()) for line in file]
    for index, line in enumerate(lines):
        previous_line = lines[index - 1]
        if line > previous_line:
            depth_increases += 1

print(f"{depth_increases} depth increases")
