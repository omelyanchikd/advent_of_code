with open('day8.txt') as file:
    signals = file.readlines()

segments = {
    (0, 1, 2, 4, 5, 6): '0',
    (2, 5): '1',
    (0, 2, 3, 4, 6): '2',
    (0, 2, 3, 5, 6): '3',
    (1, 2, 3, 5): '4',
    (0, 1, 3, 5, 6): '5',
    (0, 1, 3, 4, 5, 6): '6',
    (0, 2, 5): '7',
    (0, 1, 2, 3, 4, 5, 6): '8',
    (0, 1, 2, 3, 5, 6): '9'
}

def get_segment(digit, pattern):
    segment = []
    for element in digit:
        segment.append(pattern[element])
    return sorted(segment)

def compute_number(digits, pattern, segments):
    number = ''
    for digit in digits:
        segment = get_segment(digit, pattern)
        number += segments[tuple(segment)]
    return int(number)

def decode(inputs):
    pattern = {}
    code = {}
    for input in inputs:
        if len(input) == 2:
            code[1] = input
        if len(input) == 3:
            code[7] = input
        if len(input) == 4:
            code[4] = input
        if len(input) == 7:
            code[8] = input
        if len(input) == 5:
            for i in [2, 3, 5]:
                if i not in code:
                    code[i] = [input]
                else:
                    code[i].append(input)
        if len(input) == 6:
            for i in [0, 6, 9]:
                if i not in code:
                    code[i] = [input]
                else:
                    code[i].append(input)
    pattern[0] = list(set(code[7]) - set(code[1]))[0]
    for candidate in code[3]:
        if set(code[1]) - set(candidate) == set():
            code[3] = candidate
            code[2].remove(candidate)
            code[5].remove(candidate)
            break
    pattern_13 = set(code[4]) - set(code[1])
    pattern_46 = set(code[8]) - set(code[7]) - pattern_13
    pattern_36 = set(code[3]) - set(code[7])
    pattern[3] = list(pattern_13.intersection(pattern_36))[0]
    pattern[1] = list(pattern_13 - set(pattern[3]))[0]
    pattern[6] = list(pattern_36 - set(pattern[3]))[0]
    pattern[4] = list(pattern_46 - set(pattern[6]))[0]
    for candidate in code[2]:
        if pattern[1] in candidate:
            code[5] = candidate
            code[2].remove(candidate)
            code[2] = code[2][0]
            break
    pattern[5] = list(set(code[5]) - set(pattern[0]) - set(pattern[1]) - set(pattern[3]) - set(pattern[6]))[0]
    pattern[2] = list(set(code[2]) - set(pattern[0]) - set(pattern[4]) - set(pattern[3]) - set(pattern[6]))[0]
    return pattern

def invert(dict):
    return {value: key for key, value in dict.items()}

count_1_4_7_8 = 0
output_sum = 0

for signal in signals:
    input, output = signal.split('|')
    inputs = input.split()
    outputs = output.split()
    pattern = invert(decode(inputs))
    output_sum += compute_number(outputs, pattern, segments)
    for output in outputs:
        if len(output) in [2, 3, 4, 7]:
            count_1_4_7_8 += 1

print(f'Task 1: {count_1_4_7_8}')
print(f'Task 2: {output_sum}')



