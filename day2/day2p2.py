horizontal = 0
depth = 0
aim = 0

with open('day2input.txt') as file:
    lines = [line.strip().split() for line in file]

for line in lines:
    if line[0] == 'forward':
        horizontal = horizontal + int(line[1])
        depth = depth + aim * int(line[1])
    elif line[0] == 'down':
        aim = aim + int(line[1])
    elif line[0] == 'up':
        aim = aim - int(line[1])

print(horizontal * depth)
