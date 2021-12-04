import pandas as pd

boards = []
masks_task_1 = []
masks_task_2 = []

with open('day4.txt', 'r') as file:
    number_values = file.readline()
    lines = file.readlines()

numbers = [number for number in map(int, number_values.strip().split(','))]

input = []

for line in lines:
    if line == '\n':
        if len(input) == 0:
            continue
        board = pd.DataFrame(input).astype(int)
        boards.append(board)
        masks_task_1.append(board.isnull())
        masks_task_2.append(board.isnull())
        input = []
    else:
        input.append(line.strip().split())

last_board = pd.DataFrame(input).astype(int)
boards.append(last_board)
masks_task_1.append(last_board.isnull())
masks_task_2.append(last_board.isnull())

def bingo(df):
    return df.all(axis=1).any() or df.all(axis=0).any()

def call_numbers(numbers, boards, masks):
    for number in numbers:
        for i, board in enumerate(boards):
            masks[i] = masks[i] | (board == number)
            if bingo(masks[i]):
                return number, masks[i], board
    return number, masks[i], board

winning_number, winning_mask, winning_board = call_numbers(numbers, boards, masks_task_1)

winning_score = winning_board[~winning_mask].sum().sum()

print(f'Task 1: {winning_number * winning_score}')

def last_win(numbers, boards, masks):
    for number in numbers:
        i = 0
        while len(boards) > 0 and i < len(boards):
            masks[i] = masks[i] | (boards[i] == number)
            if bingo(masks[i]):
                if len(boards) > 1:
                    del boards[i]
                    del masks[i]
                    i -= 1
                else:
                    return number, masks[i], boards[i]
            i += 1
    return number, masks[i], boards[i]

last_number, last_mask, last_board = last_win(numbers, boards, masks_task_2)

last_winning_score = last_board[~last_mask].sum().sum()

print(f'Task 2: {last_number * last_winning_score}')
