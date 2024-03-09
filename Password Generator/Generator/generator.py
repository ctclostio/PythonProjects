# Start Generation Here
import string
import random

def generate_password(length, include_uppercase, include_lowercase, include_digits, include_special_chars):
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
    # Define the character sets to use based on the criteria
    char_sets = []
    if include_uppercase:
        char_sets.append(string.ascii_uppercase)
    if include_lowercase:
        char_sets.append(string.ascii_lowercase)
    if include_digits:
        char_sets.append(string.digits)
    if include_special_chars:
        char_sets.append(string.punctuation)
        
    # Combine the character sets into one string
    all_chars = "".join(char_sets)
    
    # Generate the password by randomly selecting characters
    password = "".join(random.choice(all_chars) for _ in range(length))
    
    return password
    def assess_password_strength(password):
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
        
        # Count the number of criteria met by the password
        criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])
        
        # Assess password strength based on the number of criteria met
        if criteria_met < 3:
            return 'Weak'
        elif criteria_met == 3:
            return 'Moderate'
        elif criteria_met == 4:
            return 'Strong'
        else:
            return 'Very Strong'












