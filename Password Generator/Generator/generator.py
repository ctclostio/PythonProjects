import string
import random
from typing import List

def generate_password(length: int, include_uppercase: bool, include_lowercase: bool,
                      include_digits: bool, include_special_chars: bool) -> str:
    """
    Generates a random password based on the specified criteria.

    Args:
        length (int): The length of the password to generate.
        include_uppercase (bool): Whether to include uppercase letters.
        include_lowercase (bool): Whether to include lowercase letters.
        include_digits (bool): Whether to include digits.
        include_special_chars (bool): Whether to include special characters.

    Returns:
        str: The generated password.
    """
    char_sets: List[str] = []
    if include_uppercase:
        char_sets.append(string.ascii_uppercase)
    if include_lowercase:
        char_sets.append(string.ascii_lowercase)
    if include_digits:
        char_sets.append(string.digits)
    if include_special_chars:
        char_sets.append(string.punctuation)

    if not char_sets:
        raise ValueError("At least one character set must be included.")

    all_chars = "".join(char_sets)
    password = "".join(random.choice(all_chars) for _ in range(length))
    return password

def assess_password_strength(password: str) -> str:
    """
    Assess the strength of the generated password based on various criteria.

    Args:
        password (str): The password to assess.

    Returns:
        str: The strength of the password ('Weak', 'Moderate', 'Strong', 'Very Strong').
    """
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = any(char in string.punctuation for char in password)

    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria,
                        digit_criteria, special_char_criteria])

    if criteria_met <= 2:
        return 'Weak'
    elif criteria_met == 3:
        return 'Moderate'
    elif criteria_met == 4:
        return 'Strong'
    else:
        return 'Very Strong'







