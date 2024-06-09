#!/usr/bin/env python
import random

# You are working in a team of developers.
# Another developer has written the code to import the names in the inputs
# You can run the code to see what this names list looks like.
# You are not allowed to use the choice() function.
# Then change the names in the input to see how it imports the names.
# print(names)
# 🚨 Remember to remove the print statement above when you submit.


def submit_names() -> list[str]:
    names = input("Insert names:\n").split(', ')
    # print(names)

    return names


def main() -> None:
    name_list = submit_names()

    index = random.randint(0, len(name_list) - 1)
    print(f"{name_list[index]} is going to buy the meal today!")


if __name__ == '__main__':
    main()
