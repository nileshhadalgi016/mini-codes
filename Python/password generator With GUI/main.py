import random
import string


def generate_password(length, complexity):
    """Generate a strong and secure password based on user specifications.

    Args:
        length (int): The desired length of the password.
        complexity (str): The desired complexity of the password. Can be 'low', 'medium', or 'high'.

    Returns:
        str: The generated password.
    """

    # Define the character sets based on complexity levels
    low_complexity = string.ascii_letters + string.digits
    medium_complexity = low_complexity + string.punctuation
    high_complexity = medium_complexity + string.ascii_uppercase

    # Select the character set based on complexity
    if complexity == 'low':
        characters = low_complexity
    elif complexity == 'medium':
        characters = medium_complexity
    elif complexity == 'high':
        characters = high_complexity
    else:
        raise ValueError("Invalid complexity level. Please choose 'low', 'medium', or 'high'.")

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


# Prompt the user for password specifications
length = int(input("Enter the desired length of the password: "))
complexity = input("Enter the desired complexity level ('low', 'medium', or 'high'): ")

# Generate the password
password = generate_password(length, complexity)
print("Generated Password:", password)
