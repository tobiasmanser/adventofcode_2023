from pathlib import Path



def main():
    cwd = Path(__file__).parent.resolve()
    input = get_input(cwd)


def get_input(cwd):
    with open(cwd / 'input.txt', 'r') as f:
        return f.readlines


main()