# Write your code below this line 👇
def prime_checker(number: int, divisor: int = 2) -> bool:
    if number <= 1:
        print("It's not a prime number.")
        return False
    if divisor > number // 2:
        print("It's a prime number.")
        return True
    if number % divisor == 0:
        print("It's not a prime number.")
        return False
    return prime_checker(number, divisor + 1)
# Write your code above this line 👆


# Do NOT change any of the code below👇
n = int(input())  # Check this number
prime_checker(number=n)
