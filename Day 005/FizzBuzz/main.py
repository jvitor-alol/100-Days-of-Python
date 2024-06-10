#!/usr/bin/env python

def main() -> None:
    # Write your code here 👇
    for num in range(1, 101):
        output = ""
        if num % 3 == 0:
            output += "Fizz"
        if num % 5 == 0:
            output += "Buzz"
        if output == "":
            output = num
        print(output)


if __name__ == '__main__':
    main()
