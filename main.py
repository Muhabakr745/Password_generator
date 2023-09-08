import random
import string


# Function to generate a random password of a given length using specified characters
def generate_random(length, chars):
    return ''.join(random.choice(chars) for _ in range(length))


# Function to get user input for 'yes' or 'no' questions
def get_user_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ('yes', 'no'):
            return user_input
        else:
            print("Please enter 'yes' or 'no'.")


# Main function
def main():
    print("Welcome to the Random Password Generator!")

    # Determine character types to include
    password_digits = get_user_input('Include digits "0123456789" (yes/no)?: ')
    password_uppercase = get_user_input('Include uppercase letters "ABCDEFGHIJKLMNOPQRSTUVWXYZ" (yes/no)?: ')
    password_lowercase = get_user_input('Include lowercase letters "abcdefghijklmnopqrstuvwxyz" (yes/no)?: ')
    password_punctuation = get_user_input('Include symbols "!#$%&*+-=?@^_" (yes/no)?: ')
    password_awkward = get_user_input('Exclude ambiguous characters "il1Lo0O" (yes/no)?: ')

    chars = ''
    digits = string.digits if password_digits == 'yes' else ''
    lowercase_letters = string.ascii_lowercase if password_lowercase == 'yes' else ''
    uppercase_letters = string.ascii_uppercase if password_uppercase == 'yes' else ''
    punctuation = '!#$%&*+-=?@^_.' if password_punctuation == 'yes' else ''

    chars += digits + lowercase_letters + uppercase_letters + punctuation

    # Exclude ambiguous characters if specified
    if password_awkward == 'yes':
        chars = chars.translate(str.maketrans('', '', 'il1Lo0O'))

    if not chars:
        print("Please select at least one character type.")
        return

    # Get user input for the number of passwords and their length
    password_quantity = int(input('Enter the number of passwords to generate: '))
    password_length = int(input('Enter the length of each password: '))

    if password_quantity <= 0 or password_length <= 0:
        print("Please enter valid quantities and lengths.")
        return

    passwords = []

    # Generate the specified number of passwords
    for _ in range(password_quantity):
        password = generate_random(password_length, chars)
        passwords.append(password)

    # Display the generated passwords
    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, 1):
        print(f"Password {i}: {password}")


if __name__ == "__main__":
    main()
