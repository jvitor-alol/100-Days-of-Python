import time
import sys


def spinning_loader(message: str, seconds: int, color_option: int = 2) -> None:
    sys.stdout.write("\033[?25l")  # Hide the cursor
    for _ in range(seconds):
        for symbol in ['\\', '|', '/', '-']:
            print(
                f"\033[3{color_option}m{message} {symbol}", end="", flush=True)
            time.sleep(0.25)
            sys.stdout.write('\033[2K\r')
    sys.stdout.write("\033[?25h")  # Show the cursor


def three_dots_message(message: str, color_option: int = 2) -> None:
    print(f"\033[3{color_option}m{message}", end='', flush=True)
    time.sleep(0.5)
    for _ in range(3):
        print(".", end='', flush=True)
        time.sleep(0.5)
    else:
        sys.stdout.write('\033[2K\r')
