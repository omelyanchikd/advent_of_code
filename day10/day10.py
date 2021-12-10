import pandas as pd

with open('day10.txt', 'r') as file:
    lines = file.readlines()

error_scores = {
    '': 0,
    ')': 3,
    '}': 1197,
    ']': 57,
    '>': 25137
}

def find_corrupt_characters(line):
    closing_brackets = [')', ']', '}', '>']
    brackets_relations = {
        '}': '{',
        ']': '[',
        ')': '(',
        '>': '<'
    }
    brackets = []
    for character in line:
        if character in closing_brackets:
            if len(brackets) == 0:
                return character
            if brackets[-1] != brackets_relations[character]:
                return character
            brackets.pop()
        else:
            brackets.append(character)
    return brackets

error_score = 0

incomplete_lines = []

for line in lines:
    erroneous_character = find_corrupt_characters(line.strip())
    if isinstance(erroneous_character, list):
        incomplete_lines.append(erroneous_character)
    else:
        error_score += error_scores[erroneous_character]

print(f'Task 1: {error_score}')

autocomplete_scores = {
    ')': 1,
    '}': 3,
    ']': 2,
    '>': 4
}

autocompletes = []

def complete_line(line):
    brackets_relations = {
        '{': '}',
        '[': ']',
        '(': ')',
        '<': '>'
    }
    completed_line = []
    for i in range(len(line)-1, -1, -1):
        completed_line += brackets_relations[line[i]]
    return completed_line

def compute_autocomplete_score(line, scores):
    score = 0
    for element in line:
        score = score * 5 + scores[element]
    return score


for line in incomplete_lines:
    completed_line = complete_line(line)
    autocomplete_score = compute_autocomplete_score(completed_line, autocomplete_scores)
    autocompletes.append(autocomplete_score)

scores = pd.Series(autocompletes)

print(f'Task 2: {scores.median()}')



