with open('day6_test.txt', 'r') as file:
    fish_ages = file.readline().strip().split(',')

fish = [int(i) for i in fish_ages]

days = 256

born_at = {day: 0 for day in range(-9, days)}

for single_fish in fish:
    born_at[single_fish] += 1

for day in range(days):
    born_at[day] = born_at[day] + born_at[day - 7] + born_at[day - 9]

print(f'Task 1: {sum([born_at[i] for i in range(80)]) + len(fish)}')

print(f'Task 2: {sum([born_at[i] for i in range(days)]) + len(fish)}')