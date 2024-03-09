# Start Generation Here
import generator

def main():
    print("Welcome to the Password Generator!")
    
    # Get user input for password criteria
    length = int(input("Enter the desired password length: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    
    # Generate the password
    password = generator.generate_password(length, include_uppercase, include_lowercase, 
                                           include_digits, include_special_chars)
    
    # Display the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
