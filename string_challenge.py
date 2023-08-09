"""
This module provides support for type hints and annotations in Python code.
"""

from typing import Any


def string_challenge(str_param: Any) -> bool:
    """
    Checks if there is an 'a' character in the string that is followed by 'b' by exactly 3 space's distance.

    Args:
        str_param: The input string to check.

    Returns:
        True if there is an 'a' character followed by 'b' at index+4 position, False otherwise.
    """
    # Loop through characters in the string using enumerate to get both indx and char
    for i, char in enumerate(str_param):
        # Check if the current char is 'a'
        if char == 'a':
            # Check if 'b' is at the indx+4 position of 'a'
            if i + 4 < len(str_param) and str_param[i+4] == 'b':
                return True
    return False


# Test cases
# Output: False
#print(string_challenge("after badly"))
# Output: True
#print(string_challenge("Laura sobs"))
