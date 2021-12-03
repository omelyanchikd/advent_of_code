input = []

with open('day1.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    input.append(int(line))

increases = 0

for i in range(1, len(input)):
    if input[i] > input[i-1]:
        increases += 1

print(f'Increases: {increases}')

triple_sums = []
triple_increases = 0

for i in range(len(input) - 2):
    triple_sums.append(input[i] + input[i+1] + input[i+2])

for i in range(1, len(triple_sums)):
    if triple_sums[i] > triple_sums[i-1]:
        triple_increases += 1


print(f'Triple increases: {triple_increases}')

