#!/usr/bin/env python

def main() -> None:
    target = int(input())  # Enter a number between 0 and 1000
    # 🚨 Do not change the code above ☝️

    # Write your code here 👇
    even_sum = 0
    for num in range(2, target + 1, 2):
        even_sum += num
    print(even_sum)


if __name__ == '__main__':
    main()
