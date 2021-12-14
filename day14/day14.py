with open('day14.txt', 'r') as file:
    template = file.readline().strip()
    file.readline()
    lines = file.readlines()

rules = {}
characters_set = set()

for line in lines:
    pair, insertion = line.strip().split(' -> ')
    rules[pair] = insertion
    characters_set.add(insertion)
    characters_set.add(pair[0])
    characters_set.add(pair[1])

template_dict = dict.fromkeys(rules.keys(), 0)
characters = dict.fromkeys(characters_set, 0)

for character in template:
    characters[character] += 1

for pair in template_dict:
    template_dict[pair] += template.count(pair)

def insert_pair(pair, insertion, new_dict, template_dict):
    pair_1 = pair[0] + insertion
    pair_2 = insertion + pair[1]
    new_dict[pair_1] += template_dict[pair]
    new_dict[pair_2] += template_dict[pair]
    return new_dict

def apply_insertions(template_dict, characters, rules):
    new_dict = dict.fromkeys(template_dict.keys(), 0)
    for pair, insertion in rules.items():
        if template_dict[pair] > 0:
            characters[insertion] += template_dict[pair]
            new_dict = insert_pair(pair, insertion, new_dict, template_dict)
    return characters, new_dict

steps = 40

for step in range(steps):
    characters, template_dict = apply_insertions(template_dict, characters, rules)

first_element = list(characters.keys())[0]

most_common_element, most_common = first_element, characters[first_element]
least_common_element, least_common = first_element, characters[first_element]

for element, count in characters.items():
    if count > most_common:
        most_common_element = element
        most_common = count
    if count < least_common:
        least_common_element = element
        least_common = count

print(characters)
print(f'Task 1: {most_common - least_common}')

