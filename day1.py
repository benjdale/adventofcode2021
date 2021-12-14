depth_increases = 0

with open("data/day1.txt") as file:
    lines = file.readlines()
    for index, line in enumerate(lines):
        line = int(line.strip())
        previous_line = int(lines[index - 1].strip())
        if line > previous_line:
            print(str(line) + " > " + str(previous_line) + " (increased)")
            depth_increases += 1
        else:
            print(str(line) + " < " + str(previous_line) + " (decreased)")

print(f"{depth_increases} depth increases")
