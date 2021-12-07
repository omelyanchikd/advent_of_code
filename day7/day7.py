import pandas as pd

with open('day7.txt', 'r') as file:
    input = file.readline().strip().split(',')

crabs = [int(i) for i in input]
crabs_series = pd.Series(crabs)
middle_ground = crabs_series.median()

def compute_fuel_1(points, position):
    fuel = 0
    for point in points:
        fuel += abs(position - point)
    return fuel

print(f'Task 1: {compute_fuel_1(crabs, middle_ground)}')

def compute_fuel_2(points, position):
    fuel = 0
    for point in points:
        distance = abs(position - point)
        fuel += (distance * (distance + 1)) / 2
    return fuel

sorted_crabs = sorted(crabs_series.unique().tolist())

minimal_fuel = float('inf')

for i in range(sorted_crabs[0], sorted_crabs[-1] + 1):
    fuel = compute_fuel_2(crabs, i)
    if fuel < minimal_fuel:
        minimal_fuel = fuel

print(f'Task 2: {minimal_fuel}')
