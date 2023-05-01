def int_to_roman(n):
    """
    1. Receive number from the user.
    2. Convert it to Roman numerals.
    """

    roman_numerals = {1000: 'M', 900: 'CM', 500: 'D',
                      400: 'CD', 100: 'C', 90: 'XC',
                      50: 'L', 40: 'XL', 10: 'X',
                      9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    roman = ''
    k = n
    for value, numeral in roman_numerals.items():
        while n >= value:
            roman += numeral
            n -= value
    print(k, " equals to ", roman)


number = int(input("Number: "))
if __name__ == "__main__":
    int_to_roman(number)
