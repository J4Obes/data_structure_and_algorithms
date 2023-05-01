def sum_even_numbers(my_list):
    """
    1. Take the list from the user.
    2. Check for the even numbers in the list.
    3. Sum all the even numbers detcted.
    4. Print the sum of the even numbers.
    """

    sum = 0
    for m in my_list:
        if m % 2 == 0:
            sum += m
    return sum


my_list = [15, 42, 13, 4, 7, 9, 10, 90, 56, 52]
if __name__ == "__main__":
    p = sum_even_numbers(my_list)
    print("Sum of even intergers:", p)
