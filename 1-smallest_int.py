def get_smallest_integer(my_list):
    """ 1. Take the list from the user.
    2. Assigne the first number in a list to the variable.
    3. Iterate to check if assigned number is less than any one in the list.
    4. If found, it is assigned to the variable untill the end of iteration.
    5. The last nuber found to be minimum is then displayed.
    """

    minimum = my_list[0]
    n = len(my_list)
    for m in range(0, n):
        if my_list[m] < minimum:
            minimum = my_list[m]
    return minimum


my_list = [34, 67, 9, 32, 3, 89, 1, 800, 674, 8]
if __name__ == "__main__":
    minimum = get_smallest_integer(my_list)
    print(minimum)
