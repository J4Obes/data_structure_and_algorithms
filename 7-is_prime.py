def is_prime(number):
    """
    1. Get the number from the user.
    2. Check if it is less than 2, if it is less than two then it is not prime.
    3. If it is greater or equal to 2, find the square root of the number.
    4. Iterate to check if the number is divisible by any number
    less than its square root.
    5. If not then it is prime, else then it is not prime.
    """

    if number < 2:
        return False
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
    return True


if __name__ == "__main__":
    number = int(input("Prime number: "))
    if is_prime(number):
        print("True")
    else:
        print("False")
