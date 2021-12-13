import pandas as pd

with open('day13.txt', 'r') as file:
    lines = file.readlines()

coordinates = []
instructions = []

line = lines.pop(0)

while line != '\n':
    x, y = line.strip().split(',')
    coordinates.append((int(x), int(y)))
    line = lines.pop(0)

for line in lines:
    axis, steps = line.strip().replace('fold along ', '').split('=')
    instructions.append((axis, int(steps)))

max_x = max([coordinate[0] for coordinate in coordinates]) + 1
max_y = max([coordinate[1] for coordinate in coordinates]) + 1

board = [[0 for i in range(max_y)] for j in range(max_x)]

for coordinate in coordinates:
    board[coordinate[0]][coordinate[1]] += 1

board = pd.DataFrame(board)

def apply_instruction(instruction, board):
    axis, steps = instruction
    if axis == 'x':
        new_board = board.loc[board.index < steps]
        last_fold = min(board.shape[0] - 1, 2 * steps + 1)
        folded_board = board.loc[[i for i in range(last_fold, steps, -1)]]
        if new_board.shape[0] > folded_board.shape[0]:
            additional_rows = pd.DataFrame(
                np.zeros((new_board.shape[0] - folded_board.shape[0], folded_board.shape[1])),
                columns = folded_board.columns
            )
            folded_board = pd.concat([additional_rows, folded_board])
        folded_board = folded_board.reset_index(drop=True)
    else:
        new_board = board[[i for i in range(steps)]]
        last_fold = min(board.shape[1]-1, 2 * steps + 1)
        folded_board = board[[i for i in range(last_fold, steps, -1)]]
        if new_board.shape[1] > folded_board.shape[1]:
            additional_columns = pd.DataFrame(
                np.zeros((folded_board.shape[0], folded_board.shape[1] - new_board.shape[1])),
                index=folded_board.index
            )
            folded_board = additional_columns.join(folded_board)
        folded_board.columns = [i for i in range(new_board.shape[1])]
    return new_board.add(folded_board)

first_board = apply_instruction(instructions[0], board)

print(f'Task 1: {(first_board > 0).sum().sum()}')

for instruction in instructions:
    print(instruction)
    board = apply_instruction(instruction, board)



