from pathlib import Path


CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def main():
    cwd = Path(__file__).parent.resolve()
    input = get_input(cwd)
    print(valid_games(input))
    print(min_needed_cubes(input))


def get_input(path):
    games = []
    with open(path / 'input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            game = int(line.split(':')[0].split()[1])
            moves = line.split(':')[1].split(';')
            games.append({'Game': game, 'Moves': moves})
    return games

def valid_games(input):
    sum = 0
    for game in input:
        valid = True
        for moves in game['Moves']:
            for move in moves.split(','):
                if int(move.split()[0]) > CUBES[move.split()[1]]:
                    valid = False
        if valid == True:
            sum += game['Game']
    return sum

def min_needed_cubes(input):
    power = 0
    for game in input:
        min_cubes = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for moves in game['Moves']:
            for move in moves.split(','):
                if int(move.split()[0]) > min_cubes[move.split()[1]]:
                    min_cubes[move.split()[1]] = int(move.split()[0])
        power += min_cubes['blue'] * min_cubes['green'] * min_cubes['red']
    return power
    
main()