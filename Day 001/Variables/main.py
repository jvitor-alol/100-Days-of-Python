def input_length():
    word = input()
    print("{} has {} letters".format(word, len(word)))


def switch_variables():
    # There are two variables, a and b from input
    a = input()
    b = input()
    # 🚨 Don't change the code above ☝️
    ####################################
    # Write your code below this line 👇
    c = a
    a = b
    b = c

    # 🚨 Don't change the code below 👇
    print("a: " + a)
    print("b: " + b)


def main() -> None:
    print("Input Length Count")
    input_length()
    print("\nSwitch variables:")
    switch_variables()


if __name__ == '__main__':
    main()
