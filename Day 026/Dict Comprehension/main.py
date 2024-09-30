#!/usr/bin/env python
from argparse import ArgumentParser


def word_size_count(sentence: str) -> None:
    result = {word: len(word) for word in sentence.split(' ')}
    print(result)


def weather_in_fahrenheit(weather_c: dict[str, int]) -> None:
    def f_convert(temp_c: int) -> float:
        return (temp_c * 9/5) + 32

    weather_f = {day: f_convert(temp_c) for day, temp_c in weather_c.items()}
    print(weather_f)


def main() -> None:
    parse = ArgumentParser()
    parse.add_argument(
        "-o", "--option",
        type=int, choices=range(2), default=0,
        help="choose function")
    args = parse.parse_args()

    match args.option:
        case 0:
            word_size_count(
                "What is the Airspeed Velocity of an Unladen Swallow?")
        case 1:
            weather_in_fahrenheit(
                {
                    "Monday": 12,
                    "Tuesday": 14,
                    "Wednesday": 15,
                    "Thursday": 14,
                    "Friday": 21,
                    "Saturday": 22,
                    "Sunday": 24
                })
        case _:
            print("Insert a valid option: {0, 1, 2}")


if __name__ == '__main__':
    main()
