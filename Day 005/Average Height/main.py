#!/usr/bin/env python

def main() -> None:
    # Input a Python list of student heights
    student_heights = input().split()
    # for n in range(0, len(student_heights)):
    #     student_heights[n] = int(student_heights[n])

    # You should not use the sum() or len() functions in your answer.
    # You should try to replicate their functionality
    # using what you have learnt about for loops.
    # 🚨 Don't change the code above 👆

    # Write your code below this row 👇
    student_heights = map(int, student_heights)

    total_height, num_of_students = 0, 0
    for height in student_heights:
        total_height += height
        num_of_students += 1

    average_height = round(total_height / num_of_students)

    print(f"total height = {total_height}")
    print(f"number of students = {num_of_students}")
    print(f"average height = {average_height}")


if __name__ == '__main__':
    main()
