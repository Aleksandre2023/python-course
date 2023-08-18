# # # Task 1
# # import random
# # import string

# # def generate_random_password():
# #     # Define the character sets for different parts of the password
# #     lowercase_letters = string.ascii_lowercase
# #     uppercase_letters = string.ascii_uppercase
# #     digits = string.digits
# #     punctuation = '@#$%&*'

# #     # Generate the first nine characters of the password
# #     first_nine_characters = (
# #         random.choices(lowercase_letters + uppercase_letters + digits, k=9)
# #     )

# #     # Generate the last character of the password
# #     last_character = random.choice(punctuation)

# #     # Combine the characters to form the final password
# #     password = ''.join(first_nine_characters) + last_character

# #     return password

# # # Generate and print a random password
# # random_password = generate_random_password()
# # print(random_password)

# # Task 2
import random
import string

def generate_random_password(length):
    # Define the character sets for different parts of the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    punctuation = '@#$%&*'

    # Generate the first part of the password
    first_part = (
        random.choices(lowercase_letters + uppercase_letters + digits, k=length - 1)
    )

    # Generate the last character of the password
    last_character = random.choice(punctuation)

    # Combine the characters to form the final password
    password = ''.join(first_part) + last_character

    return password

# Get the desired password length from the user
desired_length = int(input("Enter the desired password length: "))

# Generate and print a random password of the desired length
random_password = generate_random_password(desired_length)
print(random_password)

# Task 3
import random
import string

def generate_random_password(length):
    # Define the character sets for different parts of the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Generate the first part of the password
    first_part = (
        random.choices(lowercase_letters + uppercase_letters + digits, k=length - 1)
    )

    # Generate the last character of the password
    last_character = random.choice(punctuation)

    # Combine the characters to form the final password
    password = ''.join(first_part) + last_character    

    return password

# Get the desired password length from the user
desired_length = int(input("Enter the desired password length: "))

# Generate and print a random password of the desired length
random_password = generate_random_password(desired_length)
print(random_password)
