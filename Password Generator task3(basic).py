import random
import string

def generate_passwords(pw_lengths):
    """Generate a list of passwords based on the given lengths."""
    passwords = []
    
    for length in pw_lengths:
        password = generate_password(length)
        password = replace_with_number(password)
        password = replace_with_uppercase(password)
        password = replace_with_symbol(password)  # Adding symbols to password
        passwords.append(password)
    
    return passwords

def generate_password(length):
    """Generate a random password of the specified length."""
    if length < 3:
        print("Password length must be at least 3 characters. Setting to 3.")
        length = 3  # Ensuring minimum length of 3
    
    alphabet = string.ascii_lowercase  # Use lowercase letters
    password = ''.join(random.choice(alphabet) for _ in range(length))
    return password

def replace_with_number(pword):
    """Randomly replace one character in the password with a number."""
    replace_index = random.randrange(len(pword))  # Random index
    number = random.choice(string.digits)  # Random digit between 0-9
    pword = pword[:replace_index] + number + pword[replace_index + 1:]
    return pword

def replace_with_uppercase(pword):
    """Randomly replace one character in the password with an uppercase letter."""
    replace_index = random.randrange(len(pword))  # Random index
    uppercase = random.choice(string.ascii_uppercase)  # Random uppercase letter
    pword = pword[:replace_index] + uppercase + pword[replace_index + 1:]
    return pword

def replace_with_symbol(pword):
    """Randomly replace one character in the password with a special symbol."""
    symbols = string.punctuation  # Special symbols like @, #, $, etc.
    replace_index = random.randrange(len(pword))  # Random index
    symbol = random.choice(symbols)  # Random symbol
    pword = pword[:replace_index] + symbol + pword[replace_index + 1:]
    return pword

def get_password_lengths(num_passwords):
    """Get password lengths from the user with error handling."""
    password_lengths = []
    print("Minimum password length is 3 characters.")
    
    for i in range(num_passwords):
        while True:
            try:
                length = int(input(f"Enter the length for Password #{i + 1}: "))
                
                if length < 3:
                    print("Password length must be at least 3. Setting to 3.")
                    length = 3  # Ensure minimum length is 3
                
                password_lengths.append(length)
                break  # Break out of the loop if valid length is entered
            except ValueError:
                print("Oops! Please enter a valid integer for password length.")
    
    return password_lengths

def main():
    """Main function to run the password generation process."""
    while True:
        try:
            num_passwords = int(input("How many passwords do you want to generate? "))
            
            if num_passwords <= 0:
                print("Please enter a positive number for the number of passwords.")
                continue  # Ask again if input is invalid
            
            print(f"Generating {num_passwords} passwords...\n")
            password_lengths = get_password_lengths(num_passwords)
            
            passwords = generate_passwords(password_lengths)

            print("\nHere are your generated passwords:")
            for i, password in enumerate(passwords, 1):
                print(f"Password #{i}: {password}")
            
            # Ask the user if they want to generate more passwords
            play_again = input("\nWould you like to generate more passwords? (yes/no): ").strip().lower()
            if play_again != 'yes':
                print("Thanks for using the password generator. Goodbye!")
                break  # Exit the program

        except ValueError:
            print("Oops! That was not a valid number. Please try again.")

if __name__ == "__main__":
    main()
