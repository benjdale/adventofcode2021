with open("day3input.txt") as file:
    lines = [list(line.strip()) for line in file]

index_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

for line in lines:
    for i in range(1, 13):
        index_count[i] = index_count[i] + int(line[i - 1])

gamma = ""
for i in range(1, 13):
    if index_count[i] > 500:
        gamma = gamma + str(1)
    else:
        gamma = gamma + str(0)

power_consumption = ""
for i in range(1, 13):
    if index_count[i] > 500:
        power_consumption = power_consumption + str(0)
    else:
        power_consumption = power_consumption + str(1)

gamma = int(gamma, 2)
power_consumption = int(power_consumption, 2)

print(gamma * power_consumption)