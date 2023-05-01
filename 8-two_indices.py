def two_indices(nums, target):
    """
    1. Take the list and the target from the user.
    2. Check for the number of integers exist in a list.
    3. Iterate to sum each number in a list adding to another in a list.
    4. If their sum equals to the target then return their indices.
    """


    n = len(nums)
    for i in range(0, n):
        for j in range(0, n):
            if nums[i] + nums[j] == target:
                p = i
                q = j
                print("[", p, ", ", q, "]", end=" ")

nums = [0, 14, 5, 9, 2, 7, 1, 12, 10, 15, 78, 90]
target = 25
if __name__ == "__main__":
    two_indices(nums, target)
