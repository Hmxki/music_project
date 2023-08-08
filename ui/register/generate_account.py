import random

def generate_nonzero_start_account(length):
    first_digit = random.randint(1, 9)  # Generate a random digit from 1 to 9 for the first position
    rest_digits = ''.join(str(random.randint(0, 9)) for _ in range(length - 1))
    account = str(first_digit) + rest_digits
    return account