x = 0
y = 0

with open('day2.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    direction, distance = line.split()
    distance = int(distance)
    if direction == 'forward':
        x += distance
    if direction == 'down':
        y += distance
    if direction == 'up':
        y -= distance

print(f'Task 1: {x * y}')

x = 0
y = 0
z = 0

for line in lines:
    direction, distance = line.split()
    distance = int(distance)
    if direction == 'forward':
        x += distance
        y += (z * distance)
    if direction == 'down':
        z += distance
    if direction == 'up':
        z -= distance

print(f'Task 2: {x * y}')
