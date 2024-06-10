#!/usr/bin/env python

def main() -> None:
    # You are not allowed to use the max or min functions.
    # The output words must match the example. i.e
    # The highest score in the class is : x

    # Input a list of student scores
    student_scores = input().split()
    for n in range(0, len(student_scores)):
        student_scores[n] = int(student_scores[n])

    # Write your code below this row 👇
    max_score = student_scores[0]
    for score in student_scores:
        max_score = score if score >= max_score else max_score

    print(f"The highest score in the class is: {max_score}")


if __name__ == '__main__':
    main()
