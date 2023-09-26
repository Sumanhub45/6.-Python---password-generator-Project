
import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Invalid criteria. Please select at least one character type."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    
    while True:
        try:
            length = int(input("Enter password length: "))
            use_letters = input("Include letters? (y/n): ").lower() == "y"
            use_numbers = input("Include numbers? (y/n): ").lower() == "y"
            use_symbols = input("Include symbols? (y/n): ").lower() == "y"

            password = generate_password(length, use_letters, use_numbers, use_symbols)
            print("Generated Password:", password)

            break
        except ValueError:
            print("Invalid input. Please enter a valid password length.")

if __name__ == "__main__":
    main()
