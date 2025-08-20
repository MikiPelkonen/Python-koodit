import random

# Variables for codes
three_digit_code: list[int] = [random.randint(0, 9) for _ in range(3)]
four_digit_code: list[int] = [random.randint(1, 6) for _ in range(4)]

# Print results.
print(f"3-digit code: {''.join(map(str, three_digit_code))}")
print(f"4-digit code: {''.join(map(str, four_digit_code))}")
