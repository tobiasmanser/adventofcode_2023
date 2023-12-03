from pathlib import Path
import re









def main():
    cwd = Path(__file__).parent.resolve()
    input = get_input(cwd)
    print(engine_ratio(input))

def get_input(cwd):
    with open(cwd / 'input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines)
    return lines

def valid_numbers(lines):
    sum = 0
    for i in range(0, len(lines)):
        matches = re.finditer(r'\d+', lines[i])
        for m in matches:
            if lines[i][m.start()-1] != '.':
                sum += int(m.group())
                continue
            elif m.end() < len(lines[i]):
                if lines[i][m.end()] != '.':
                    #print(lines[i][m.end()])
                    sum += int(m.group())
                    continue
            if i + 1 < len(lines):
                for char in lines[i+1][m.start()-1:m.end()+1]:
                    #print(char)
                    if char != '.' and not char.isnumeric():
                        sum += int(m.group())
                        continue
            if i > 0:
                for char in lines[i - 1][m.start()-1:m.end()+1]:
                    if char != '.' and not char.isnumeric():
                        sum += int(m.group())
                        continue
    return sum

def engine_ratio(lines):
    ratio = 0
    for i in range(0, len(lines)):
        matches = re.finditer(r'\*', lines[i])
        for m in matches:
            found = []
            found.extend(find_engines(lines[i], m.start()))
            if i + 1 < len(lines):
                found.extend(find_engines(lines[i+1], m.start()))
            if i > 0:
                found.extend(find_engines(lines[i-1], m.start()))
            print(found)
            if len(found) == 2:
                ratio += found[0] * found[1]
    return ratio
            

def find_engines(line, star_index):
    engines = []
    numbers = re.finditer(r'\d+', line)
    for n in numbers:
        if n.start() <= star_index + 1 and n.end() > star_index - 1:
            engines.append(int(n.group()))
    return engines

main()