#!/usr/bin/env python

def main() -> None:
    two_digit_number = input()
    # 🚨 Don't change the code above 👆
    ####################################
    # Write your code below this line 👇

    digits = map(lambda x: int(x), list(two_digit_number))
    print(sum(digits))


if __name__ == '__main__':
    main()
