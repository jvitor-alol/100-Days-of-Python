import random

from termcolor import colored

from .logo import LOGO
from .verifications import check_input

CARDS = {
    'A': {
        'value': [1, 11],
        'suit': [
            '\U0001F0A1',  # Ace of Spades
            '\U0001F0B1',  # Ace of Hearts
            '\U0001F0C1',  # Ace of Diamonds
            '\U0001F0D1',  # Ace of Clubs
        ]
    },
    '2': {
        'value': 2,
        'suit': [
            '\U0001F0A2',  # 2 of Spades
            '\U0001F0B2',  # 2 of Hearts
            '\U0001F0C2',  # 2 of Diamonds
            '\U0001F0D2',  # 2 of Clubs
        ]
    },
    '3': {
        'value': 3,
        'suit': [
            '\U0001F0A3',  # 3 of Spades
            '\U0001F0B3',  # 3 of Hearts
            '\U0001F0C3',  # 3 of Diamonds
            '\U0001F0D3',  # 3 of Clubs
        ]
    },
    '4': {
        'value': 4,
        'suit': [
            '\U0001F0A4',  # 4 of Spades
            '\U0001F0B4',  # 4 of Hearts
            '\U0001F0C4',  # 4 of Diamonds
            '\U0001F0D4',  # 4 of Clubs
        ]
    },
    '5': {
        'value': 5,
        'suit': [
            '\U0001F0A5',  # 5 of Spades
            '\U0001F0B5',  # 5 of Hearts
            '\U0001F0C5',  # 5 of Diamonds
            '\U0001F0D5',  # 5 of Clubs
        ]
    },
    '6': {
        'value': 6,
        'suit': [
            '\U0001F0A6',  # 6 of Spades
            '\U0001F0B6',  # 6 of Hearts
            '\U0001F0C6',  # 6 of Diamonds
            '\U0001F0D6',  # 6 of Clubs
        ]
    },
    '7': {
        'value': 7,
        'suit': [
            '\U0001F0A7',  # 7 of Spades
            '\U0001F0B7',  # 7 of Hearts
            '\U0001F0C7',  # 7 of Diamonds
            '\U0001F0D7',  # 7 of Clubs
        ]
    },
    '8': {
        'value': 8,
        'suit': [
            '\U0001F0A8',  # 8 of Spades
            '\U0001F0B8',  # 8 of Hearts
            '\U0001F0C8',  # 8 of Diamonds
            '\U0001F0D8',  # 8 of Clubs
        ]
    },
    '9': {
        'value': 9,
        'suit': [
            '\U0001F0A9',  # 9 of Spades
            '\U0001F0B9',  # 9 of Hearts
            '\U0001F0C9',  # 9 of Diamonds
            '\U0001F0D9',  # 9 of Clubs
        ]
    },
    '10': {
        'value': 10,
        'suit': [
            '\U0001F0AA',  # 10 of Spades
            '\U0001F0BA',  # 10 of Hearts
            '\U0001F0CA',  # 10 of Diamonds
            '\U0001F0DA',  # 10 of Clubs
        ]
    },
    'J': {
        'value': 10,
        'suit': [
            '\U0001F0AB',  # Jack of Spades
            '\U0001F0BB',  # Jack of Hearts
            '\U0001F0CB',  # Jack of Diamonds
            '\U0001F0DB',  # Jack of Clubs
        ]
    },
    'Q': {
        'value': 10,
        'suit': [
            '\U0001F0AD',  # Queen of Spades
            '\U0001F0BD',  # Queen of Hearts
            '\U0001F0CD',  # Queen of Diamonds
            '\U0001F0DD',  # Queen of Clubs
        ]
    },
    'K': {
        'value': 10,
        'suit': [
            '\U0001F0AE',  # King of Spades
            '\U0001F0BE',  # King of Hearts
            '\U0001F0CE',  # King of Diamonds
            '\U0001F0DE',  # King of Clubs
        ]
    }
}


def calculate_hand(hand: list[tuple[str, str]]) -> int:
    card_names = [card[0] for card in hand]

    result = 0
    for card in sorted(card_names):
        if result <= 10 and card == 'A':
            result += CARDS['A']['value'][1]
        elif card == 'A':
            result += CARDS['A']['value'][0]
        else:
            result += CARDS[card]['value']

    return result


def has_blackjack(hand: list[tuple[str, str]]) -> bool:
    if calculate_hand(hand) == 21:
        return True
    else:
        return False


def deal_cards() -> tuple[str, str]:
    new_card = random.choice(list(CARDS.keys()))
    unicode_card = random.choice(CARDS[new_card]['suit'])

    return (new_card, unicode_card)


def evaluate_winner(player_hand: list[tuple[str, str]],
                    cpu_hand: list[tuple[str, str]]) -> None:
    _player_result = calculate_hand(player_hand)
    _cpu_result = calculate_hand(cpu_hand)
    _player_bust = True if _player_result > 21 else False
    _cpu_bust = True if _cpu_result > 21 else False

    message = '\t'

    if has_blackjack(player_hand) or has_blackjack(cpu_hand):
        message += "BLACKJACK! "
    elif _player_bust or _cpu_bust:
        message += "It's a BUST! "

    if ((has_blackjack(player_hand) and has_blackjack(cpu_hand)) or
            (_player_result == _cpu_result)):
        message += 'Draw 🙃'
    elif not _player_bust and (
            _cpu_bust or has_blackjack(player_hand)
            or _player_result > _cpu_result):
        message += 'Player Wins 😁'
    else:
        message += 'House Wins 😣'

    print(
        f"\n\tYour final hand {' '.join([t[1] for t in player_hand])}: "
        f"[{', '.join([t[0] for t in player_hand])}], "
        f"final score: {_player_result}")
    print(
        f"\tHouse's final hand {' '.join([t[1] for t in cpu_hand])}: "
        f"[{', '.join([t[0] for t in cpu_hand])}], "
        f"final score: {_cpu_result}\n")
    print(colored(message + "\n", "green", attrs=["blink"]))


__all__ = ['LOGO', 'CARDS', 'check_input', 'calculate_hand', 'has_blackjack',
           'deal_cards', 'evaluate_winner']
