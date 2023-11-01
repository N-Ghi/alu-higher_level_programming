#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = number % 10

if last_digit > 5:
    comparison_text = "and is greater than 5"
elif last_digit == 0:
    comparison_text = "and is 0"
else:
    if number < 0:
        last_digit = -last_digit
    comparison_text = "and is less than 6 and not 0"

print(f"Last digit of {number} is {last_digit_with_sign} {comparison_text}")

