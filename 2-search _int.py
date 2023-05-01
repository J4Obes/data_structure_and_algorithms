def find_first_occurrence(my_list, num):
    """
    1. Get the list and a number from the user.
    2. Check at what index does the number exist in the list.
    """
    for i in range(len(my_list)):
        if my_list[i] == num:
            return i
    return -1

my_list = [54, 12, 96, 89, 37, 69, 43, 1, 30, 86, 74, 63, 5]
number = 69
if __name__ == "__main__":
    index = find_first_occurrence(my_list, number)
    if index != -1:
        print( number, " is at index ", index)
    else:
        print(number, " not in the list.")
