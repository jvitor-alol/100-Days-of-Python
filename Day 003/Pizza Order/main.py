#!/usr/bin/env python

def main() -> None:
    pizza_prices = {
        'S': 15,
        'M': 20,
        'L': 25
    }

    print("Thank you for choosing Python Pizza Deliveries!\n")
    size = input("# What size pizza do you want? S, M, or L: ").upper()
    add_pepperoni = input("# Do you want pepperoni? Y or N: ").upper()
    extra_cheese = input("# Do you want extra cheese? Y or N: ").upper()
    # 🚨 Don't change the code above 👆
    # Write your code below this line 👇

    bill = pizza_prices[size]

    if add_pepperoni == "Y":
        if size == "S":
            bill += 2
        else:
            bill += 3
    if extra_cheese == "Y":
        bill += 1

    print(f"Your final bill is: ${bill}.")


if __name__ == '__main__':
    main()
