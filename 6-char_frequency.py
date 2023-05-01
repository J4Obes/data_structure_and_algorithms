def character_frequency(string):
    """
    1. Take the text/string in alphabets from the user ignoring non aphabets.
    2. Check for number of appearence of each character in a text.
    3. Print each character with it's number of appearence.
    """

    frequency = {}
    for char in string:
        if char.isalpha():
            char = char.lower()
            frequency[char] = frequency.get(char, 0) + 1
    return frequency


string = input("String: ")
if __name__ == "__main__":
    frequency = character_frequency(string)
    print(frequency)
