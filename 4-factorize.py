def factorize(number):
    """
    1. Take the the number from the user.
    2. Determining all the factors of the number and print them.
    """

    for n in range(1, number + 1):
        factors = []
        if number % n == 0:
            print(n, end=" ")


no = int(input("Enter any number: "))
if __name__ == "__main__":
    factorize(no)
