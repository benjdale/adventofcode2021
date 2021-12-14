depth_increases = 0

with open("../data/day1.txt") as file:
    lines = [int(line.strip()) for line in file]
    for index, line in enumerate(lines):
        try:
            final_line = lines[index+3]
        except IndexError:
            break

        current_depth = line + lines[index + 1] + lines[index + 2]
        next_depth = lines[index + 1] + lines[index + 2] + lines[index + 3]
        if current_depth < next_depth:
            depth_increases += 1

print(f"{depth_increases} depth increases")
