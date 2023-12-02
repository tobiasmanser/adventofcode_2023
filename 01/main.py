from pathlib import Path
import re

REGEX = re.compile(r"(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))", re.IGNORECASE)

written_numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def main():
    cwd = Path(__file__).parent.resolve()
    input = get_input(cwd)
    sum = get_sum(input)

    print(sum)


def get_input(path):
    with open(path / 'input.txt', 'r') as f:
        lines = f.readlines()
        return lines

def get_sum(input):
    sum = 0
    for line in input:
        numbers = []
        matches = REGEX.findall(line)
        for match in matches:
            if match.isnumeric():
                numbers.append(match)
            else:
                numbers.append(written_numbers[match])
        sum += int(numbers[0] + numbers[-1])
        print(f"{line.strip()}: {int(numbers[0] + numbers[-1])}")
    return sum

main()

