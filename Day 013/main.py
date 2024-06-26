# ########### DEBUGGING ###########

# Describe Problem
# range doesn't include 20: fix range(1, 20) -> range(1, 21)

from random import randint


def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()


# # Reproduce the Bug
# index out of range: fix dice_imgs[dice_num] -> dice_imgs[dice_num - 1]

dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_num)
print(dice_imgs[dice_num - 1])

# # Play Computer
# input 1994 not defined: fix elif year > 1994 -> elif year >= 1994
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:
    print("You are a Gen Z.")

# # Fix the Errors
# fix: indent + cast input to int + use f-string
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

# #Print is Your Friend
# fix at line 44: word_per_page == (compare) -> word_per_page = (assign)
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
print(pages)
word_per_page = int(input("Number of words per page: "))
print(word_per_page)
total_words = pages * word_per_page
print(total_words)

# #Use a Debugger
# https://pythontutor.com/visualize.html#mode=edit
# fix indentation


def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
