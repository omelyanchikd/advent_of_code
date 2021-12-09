import pandas as pd

with open('day9.txt', 'r') as file:
    lines = file.readlines()

heightmap = []
basins = []

for line in lines:
    row = [int(i) for i in list(line.strip())]
    heightmap.append(row)
    basins.append([None if row[i] != 9 else -1 for i in range(len(row))])

lowest_points = []

for i in range(len(heightmap)):
    for j in range(len(heightmap[i])):
        current_cell = heightmap[i][j]
        candidates = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        lowest_point = True
        for candidate in candidates:
            if candidate[0] < 0 or candidate[1] < 0 or candidate[0] == len(heightmap) or candidate[1] == len(heightmap[i]):
                continue
            if heightmap[candidate[0]][candidate[1]] <= current_cell:
                lowest_point = False
                break

        if lowest_point:
            lowest_points.append([i, j, current_cell])

def compute_risk_levels(lowest_points):
    risk_level = 0
    for i, j, height in lowest_points:
        risk_level += (height + 1)
    return risk_level

print(f'Task 1: {compute_risk_levels(lowest_points)}')

def points_are_neighbors(a, b):
    i, j = b[0], b[1]
    candidates = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    for candidate in candidates:
        if a == candidate:
            return True
    return False

def point_belongs_to_region(point, region):
    for element in region:
        if points_are_neighbors(point, element):
            return True
    return False

def update_regions_with_point(point, regions):
    regions_to_merge = []
    for i, region in enumerate(regions):
        if point_belongs_to_region(point, region):
            regions_to_merge.append(i)
    if len(regions_to_merge) == 0:
        regions.append([point])
    elif len(regions_to_merge) == 1:
        regions[regions_to_merge[0]].append(point)
    else:
        merged_region = [point]
        for i in regions_to_merge:
            merged_region += regions[i]
        regions = [regions[i] for i in range(len(regions)) if i not in regions_to_merge]
        regions.append(merged_region)
    return regions

basin_regions = []

for i in range(len(basins)):
    for j in range(len(basins[i])):
        if not basins[i][j]:
            basin_regions = update_regions_with_point((i, j), basin_regions)

basin_sizes = []

for basin in basin_regions:
    basin_sizes.append(len(basin))

basin_sizes = sorted(basin_sizes, key=lambda x: -x)

print(f'Task 2: {basin_sizes[0] * basin_sizes[1] * basin_sizes[2]}')


