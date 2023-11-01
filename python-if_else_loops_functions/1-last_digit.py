#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = number % 10
last_digit_with_sign = last_digit if number >= 0 else -last_digit

if last_digit_with_sign > 5:
    comparison_text = "and is greater than 5"
elif last_digit_with_sign == 0:
    comparison_text = "and is 0"
else:
    comparison_text = "and is less than 6 and not 0"

print(f"Last digit of {number} is {last_digit_with_sign} is {comparison_text}")

