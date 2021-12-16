

with open('day16_test.txt', 'r') as file:
    line = file.readlines()[0]

def convert_heximal(character):
    heximals = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }
    return heximals[character]

def get_type(type_id):
    types = {
        0: 'sum',
        1: 'product',
        2: 'min',
        3: 'max',
        4: 'value',
        5: 'greater',
        6: 'less',
        7: 'equal'
    }
    return types[type_id]

def get_bit_string(heximal):
    bit_string = ''
    for character in heximal:
        bit_string += convert_heximal(character)
    return bit_string

def parse_literal_value(line):
    signal = line[0]
    i = 0
    literal_value = ''
    while True:
        literal_value += line[(i+1):(i+5)]
        if int(signal) == 0:
            break
        i += 5
        signal = line[i]
    literal_value = int(literal_value, base=2)
    final_i = min(i+5, len(line))
    if final_i == len(line):
        return '', literal_value
    return line[final_i:], literal_value


def get_packet_info(line):
    if len(line) < 6:
        return None
    packet = {
        'version': int(line[:3], base=2),
        'type': int(line[3:6], base=2)
    }
    if packet['type'] == 4:
        return packet
    return get_length_type(line, packet)

def get_length_type(line, packet):
    if len(line) < 7:
        return None
    length_type_id = line[6]
    if (int(length_type_id) == 0 and len(line) < 23) or (int(length_type_id) == len(line) < 19):
        return None
    if int(length_type_id) == 0:
        subpacket_length = int(line[7:22], base=2)
        packet['subpacket_length'] = subpacket_length
    else:
        subpacket_count = int(line[7:18], base=2)
        packet['subpacket_count'] = subpacket_count
    return packet

def parse_bit_string(line, length=None):
    if length:
        return parse_bit_string(line[:length]) + parse_bit_string(line[length:])
    packet = get_packet_info(line)
    if not packet:
        return []
    if packet['type'] == 4:
        new_line, literal_value = parse_literal_value(line[6:])
        packet['literal_value'] = literal_value
        return [packet] + parse_bit_string(new_line)
    else:
        if 'subpacket_length' in packet:
            return [packet] + parse_bit_string(line[22:], length=packet['subpacket_length'])
        return [packet] + parse_bit_string(line[18:])
    return []

packets = []

bit_string = get_bit_string(line)
packets = parse_bit_string(bit_string)

versions = 0

for packet in packets:
    print(packet)
    if 'version' in packet:
        versions += packet['version']

print(f'Task 1: {versions}')

