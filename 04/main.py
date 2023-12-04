from pathlib import Path
import math



def main():
    cwd = Path(__file__).parent.resolve()
    cards = get_input(cwd)
    #points = points_of_cards(cards)
    nr_cards = card_multi(cards)
    print(sum(card['nr'] for card in nr_cards))


def get_input(cwd):
    with open(cwd / 'input.txt', 'r') as f:
        cards = []
        lines = f.readlines()
        for line in lines:
            cards.append({'card': int(line.split(':')[0].split()[1]), 'winning': line.split(':')[1].split('|')[0].split(), 'numbers': line.split(':')[1].split('|')[1].split(), 'nr': 1})
        return cards
    
def points_of_cards(cards):
    points_total = 0
    for card in cards:
        number_of_wins = 0
        for win in card['winning']:
            if win in card['numbers']:
                print(f"{card['card']}: {win}")
                number_of_wins += 1
        if number_of_wins != 0:
            print(card['card'], number_of_wins)
            points_total += math.pow(2, number_of_wins - 1)
    return round(points_total)

def card_multi(cards):
    cards_m = cards
    for card in cards:
        number_of_wins = 0
        for win in card['winning']:
            if win in card['numbers']:
                number_of_wins += 1
        for i in range(card['card'], card['card'] + number_of_wins):
            print(f"Added {cards_m[i]['nr']} cards to {cards[i]['card']}")
            cards_m[i]['nr'] += cards_m[card['card'] - 1]['nr']
    return cards_m
        
    
main()