#!/usr/bin/env python
import os
import sys

from termcolor import colored

from utils import LOGO
from utils import check_input, calculate_hand, deal_cards
from utils import has_blackjack, evaluate_winner


def render_game() -> str:
    _keep_playing = True

    # Starting hands
    player_hand = [deal_cards() for _ in range(2)]
    player_score = calculate_hand(player_hand)
    cpu_hand = [deal_cards() for _ in range(2)]
    cpu_score = calculate_hand(cpu_hand)

    while _keep_playing:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored(LOGO, "blue"))

        print(
            f"\tYour cards {' '.join([t[1] for t in player_hand])}: "
            f"[{', '.join([t[0] for t in player_hand])}], "
            f"current score: {player_score}")
        print(f"\tHouse's first card {cpu_hand[0][1]} 🂠: {cpu_hand[0][0]}\n")

        # In case either player starts with blackjack
        if has_blackjack(player_hand) or has_blackjack(cpu_hand):
            break

        draw_again = check_input(
            "Hit? [Y/n]: ",
            lambda x: x.lower() in ['yes', 'y', 'no', 'n'] or x == '',
            "blue")
        if draw_again in ['no', 'n']:
            _keep_playing = False  # Ends game
        else:
            player_hand.append(deal_cards())
            player_score = calculate_hand(player_hand)
            if cpu_score < 17:
                cpu_hand.append(deal_cards())
                cpu_score = calculate_hand(cpu_hand)

        # Endgame conditions
        if has_blackjack(player_hand) or has_blackjack(cpu_hand):
            _keep_playing = False
        if cpu_score > 21 or player_score > 21:
            _keep_playing = False

    evaluate_winner(player_hand, cpu_hand)
    return check_input(
        "Play again? [Y/n]: ",
        lambda x: x.lower() in ['yes', 'y', 'no', 'n'] or x == '',
        "blue")


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored(LOGO, "blue"))
    game_start = check_input(
        "Do you want to play a game of Blackjack? [Y/n]: ",
        lambda x: x.lower() in ['yes', 'y', 'no', 'n'] or x == '',
        "blue")
    if game_start in ['no', 'n']:
        print(colored("Farewell, then.", "blue"))
        sys.exit()

    replay = 'yes'
    while replay not in ['no', 'n']:
        replay = render_game()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
