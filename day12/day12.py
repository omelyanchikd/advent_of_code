import numpy as np
import pandas as pd

with open('day12.txt', 'r') as file:
    lines = file.readlines()

edges = {}
vertices = set()

def add_edge(a, b, edges):
    if a not in edges:
        edges[a] = []
    if b not in edges:
        edges[b] = []
    edges[a].append(b)
    edges[b].append(a)
    return edges

for line in lines:
    start, end = line.strip().split('-')
    vertices.add(start)
    vertices.add(end)
    edges = add_edge(start, end, edges)

small_caves = set()
large_caves = set()

for vertex in vertices:
    if vertex.islower():
        small_caves.add(vertex)
    else:
        large_caves.add(vertex)

def any_other_cave_more_than_2_visits(current_cave, caves):
    for cave, visits in caves.items():
        if visits > 1 and cave != current_cave:
            return True
    return False

def invalid_path(path, small_caves):
    small_cave_counts = dict.fromkeys(list(small_caves), 0)
    for element in path.split(','):
        if element in small_caves:
            small_cave_counts[element] += 1
            if (small_cave_counts[element] > 1 and any_other_cave_more_than_2_visits(element, small_cave_counts)) or (small_cave_counts[element] > 2):
                return True
    return False

vertex = 'start'
paths = set()

def find_path(vertex, edges, path, paths, small_caves):
    while vertex != 'end':
        neighbors = edges[vertex]
        for neighbor in neighbors:
            if neighbor == 'start':
                continue
            new_path = path + ',' + neighbor
            if new_path in paths:
                continue
            if invalid_path(new_path, small_caves):
                continue
            paths.add(new_path)
            paths |= find_path(neighbor, edges, new_path, paths, small_caves)
        return paths
    return paths

paths = find_path('start', edges, 'start', paths, small_caves)

valid_paths = 0

for path in paths:
    if 'end' in path:
        valid_paths += 1

print(f'Task 1: {valid_paths}')





