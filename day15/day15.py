import pandas as pd
import numpy as np

with open('day15_test.txt', 'r') as file:
    lines = file.readlines()

input = []

for line in lines:
  input.append([int(i) for i in list(line.strip())])

input = pd.DataFrame(input)


def dijkstra(input):
  distances = pd.DataFrame(np.ones(input.shape) * np.Infinity)
  distances.loc[0,0] = 0

  origins = pd.DataFrame([[None for i in range(input.shape[0])] for j in range(input.shape[1])])
  visited = pd.DataFrame(np.zeros(input.shape)).astype(bool)

  i, j = 0, 0

  while i != input.shape[0] - 1 or j != input.shape[1] - 1:
    candidates = [(i + 1, j), (i-1, j), (i, j-1), (i, j+1)]
    for candidate in candidates:
      if candidate[0] < 0 or candidate[0] == input.shape[0] or candidate[1] < 0 or candidate[1] == input.shape[1]:
        continue
      if visited.loc[candidate[0], candidate[1]]:
        continue
      if distances.loc[candidate[0], candidate[1]] > input.loc[candidate[0], candidate[1]] + distances.loc[i, j]:
        distances.loc[candidate[0], candidate[1]] = input.loc[candidate[0], candidate[1]] + distances.loc[i, j]
        origins.loc[candidate[0], candidate[1]] = (i, j)
    visited.loc[i, j] = True

    j = distances[~visited].idxmin(axis=1).min()
    i = distances[~visited][j].idxmin()
  return distances.loc[input.shape[0]-1, input.shape[1]-1]

print(f'Task 1: {dijkstra(input)}')

def increase_risk_level(df):
  df = df.add(1)
  df[df > 9] = 1
  return df

map_row = pd.concat([
  input,
  increase_risk_level(input),
  increase_risk_level(increase_risk_level(input)),
  increase_risk_level(increase_risk_level(increase_risk_level(input))),
  increase_risk_level(increase_risk_level(increase_risk_level(increase_risk_level(input))))
  ],
  axis=1,
  ignore_index=True
)

real_map = pd.concat([
  map_row,
  increase_risk_level(map_row),
  increase_risk_level(increase_risk_level(map_row)),
  increase_risk_level(increase_risk_level(increase_risk_level(map_row))),
  increase_risk_level(increase_risk_level(increase_risk_level(increase_risk_level(map_row))))
  ],
  axis=0,
  ignore_index=True
).reset_index(drop=True)

print(f'Task 2: {dijkstra(real_map)}')



