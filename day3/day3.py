import pandas as pd

input = []

with open('day3.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    input.append(list(line.strip()))

df = pd.DataFrame(input).astype(int)

gamma_rate_values = df.mode(axis=0).squeeze().astype(str).tolist()
epsilon_rate_values = [str(int(not int(char))) for char in gamma_rate_values]

gamma_rate = int(''.join(gamma_rate_values), 2)
epsilon_rate = int(''.join(epsilon_rate_values), 2)

print(f'Task 1: {gamma_rate * epsilon_rate}')

def filter_bits(df, reverse_mode = False):
    mask = pd.Series([True] * df.shape[0])
    for column in df.columns:
        if df[mask].shape[0] == 1:
            return df[mask].astype(str).squeeze().tolist()
        mode = df[mask][column].mode().squeeze()
        if isinstance(mode, pd.Series):
            mode = 1
        if reverse_mode:
            mode = int(not mode)
        mask = mask & (df[column] == mode)
    return df[mask].astype(str).squeeze().tolist()

oxygen_values = filter_bits(df)
co2_values = filter_bits(df, reverse_mode=True)

oxygen_rate = int(''.join(oxygen_values), 2)
co2_rate = int(''.join(co2_values), 2)

print(f'Task 1: {oxygen_rate * co2_rate}')


