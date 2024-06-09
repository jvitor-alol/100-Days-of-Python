#!/usr/bin/env python

def main() -> None:
    treasure_map = [["⬜️"] * 3 for _ in range(3)]

    print("Hiding your treasure! X marks the spot.")
    print("-------A------B-----C------")
    [print(f"{i+1} - {line}") for i, line in enumerate(treasure_map)]

    inserted_position = input("Select a position for column and line (A1): ")\
        .lower()
    real_position = (
        int(inserted_position[1]) - 1,
        ('a', 'b', 'c').index(inserted_position[0]))

    treasure_map[real_position[0]][real_position[1]] = 'X'
    [print(f"{i+1} - {line}") for i, line in enumerate(treasure_map)]


if __name__ == '__main__':
    main()
