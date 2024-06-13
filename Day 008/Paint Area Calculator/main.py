# Write your code below this line 👇
from math import ceil
from typing import Union


def paint_calc(height: Union[float, int], width: Union[float, int],
               cover: Union[float, int] = 5.0) -> int:
    num_cans = ceil((height * width) / cover)
    print(f"You'll need {num_cans} cans of paint.")
    return num_cans
# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.


# 🚨 Don't change the code below 👇
test_h = int(input())  # Height of wall (m)
test_w = int(input())  # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
