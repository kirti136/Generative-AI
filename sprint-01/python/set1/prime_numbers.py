def is_prime(number):
    if number <= 1:
        return f"{number} is not a prime number."
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return f"{number} is not a prime number."
    return f"{number} is a prime number."

number = 13
output = is_prime(number)
print(output)
