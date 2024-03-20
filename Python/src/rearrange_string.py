"""
Given a string, write a function named rearrange_string that performs the following:
Removes all digits.
Converts all uppercase letters to lowercase.
Reverses the string.
"""


def rearrange_string(s):
    # Remove digits
    s = "".join(char for char in s if not char.isdigit())

    # Convert uppercase letters to lowercase
    s = s.lower()

    # Reverse the string
    s = s[::-1]

    return s


if __name__ == "__main__":
    s = "AbC123DeF"
    s_modify = rearrange_string(s)
    print(s_modify)
