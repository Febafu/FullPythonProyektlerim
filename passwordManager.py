import os
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def save_password(service, username, password, file_path="passwords.txt"):
    with open(file_path, "a") as f:
        f.write(f"{service} | {username} | {password}\n")

def main():
    print("Password Manager")
    while True:
        print("\n1. Generate Password\n2. Save Password\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            length = int(input("Enter password length: "))
            print("Generated Password:", generate_password(length))
        elif choice == "2":
            service = input("Enter service name: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            save_password(service, username, password)
            print("Password saved successfully!")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
