import math


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
while True:  
    number = input("Enter a number to check if it's prime (or type 'exit' to stop): ")
    if number.lower() == 'exit':
        print("Exiting the program.")
        break
    number = int(number)
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")