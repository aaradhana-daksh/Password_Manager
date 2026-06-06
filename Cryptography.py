from cryptography.fernet import Fernet
import os

# Generate key (run only once)
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load key
def load_key():
    return open("secret.key", "rb").read()

# Create key if not exists
if not os.path.exists("secret.key"):
    generate_key()

key = load_key()
fernet = Fernet(key)

# Add Password
def add_password():
    account = input("Enter Account Name: ")
    password = input("Enter Password: ")

    encrypted_password = fernet.encrypt(password.encode())

    with open("passwords.txt", "ab") as file:
        file.write(account.encode() + b"|" + encrypted_password + b"\n")

    print("Password Saved Successfully!")

# View Password
def view_password():
    if not os.path.exists("passwords.txt"):
        print("No passwords stored.")
        return

    with open("passwords.txt", "rb") as file:
        for line in file.readlines():
            data = line.strip().split(b"|")
            account = data[0].decode()
            decrypted_password = fernet.decrypt(data[1]).decode()

            print(f"Account: {account}")
            print(f"Password: {decrypted_password}")
            print("-" * 30)

# Main Menu
while True:
    print("\n===== Password Manager =====")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_password()
    elif choice == "2":
        view_password()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice!")
        
