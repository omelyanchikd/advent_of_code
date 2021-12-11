octopuses = []

with open('day11.txt', 'r') as file:
    lines = file.readlines()

steps = 100

for line in lines:
    octopuses_row = [int(i) for i in line.strip()]
    octopuses.append(octopuses_row)

flashes = 0

def flash_octopuses(octopus, octopuses, new_octopuses, flashed_octopuses, flashes):
    i, j = octopus
    if octopuses[i][j] > 9:
        octopuses[i][j] = 0
        flashed_octopuses.add((i, j))
        flashes += 1
        neighbors = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j+1), (i+1, j+1), (i+1, j), (i+1, j-1), (i, j-1)]
        for neighbor in neighbors:
            if neighbor[0] < 0 or neighbor[1] < 0 or neighbor[0] == len(octopuses) or neighbor[1] == len(octopuses):
                continue
            if neighbor not in flashed_octopuses:
                new_octopuses.add(neighbor)
                octopuses[neighbor[0]][neighbor[1]] += 1
    return new_octopuses, flashed_octopuses, octopuses, flashes

def check_sync(octopuses):
    return sum([sum(octopuses_row) for octopuses_row in octopuses]) == 0

for step in range(steps):
    new_octopuses = set()
    flashed_octopuses = set()
    for i in range(len(octopuses)):
        for j in range(len(octopuses[i])):
            octopuses[i][j] += 1
            if octopuses[i][j] > 9:
                new_octopuses.add((i, j))
    while new_octopuses:
        octopus = new_octopuses.pop()
        new_octopuses, flashed_octopuses, octopuses, flashes = flash_octopuses(octopus, octopuses, new_octopuses, flashed_octopuses, flashes)

print(f'Task 1: {flashes}')

while not check_sync(octopuses):
    steps += 1
    new_octopuses = set()
    flashed_octopuses = set()
    for i in range(len(octopuses)):
        for j in range(len(octopuses[i])):
            octopuses[i][j] += 1
            if octopuses[i][j] > 9:
                new_octopuses.add((i, j))
    while new_octopuses:
        octopus = new_octopuses.pop()
        new_octopuses, flashed_octopuses, octopuses, flashes = flash_octopuses(octopus, octopuses, new_octopuses, flashed_octopuses, flashes)

print(f'Task 2: {steps}')


