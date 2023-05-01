def print_right_triangle(height):
    """
    1. Take the height from the user.
    2. Print stars according to the height.
    """

    for i in range(1, height + 1):
        for j in range(1, height + 1):
            if i >= j:
                print("*", end="")
            else:
                print(" ", end="")
        print("\n")


height = int(input("Height: "))
if __name__ == "__main__":
    print_right_triangle(height)
