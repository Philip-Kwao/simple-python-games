from cryptography.fernet import Fernet 

def create_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

def write_pass():
    key = load_key()
    fer = Fernet(key)
    username = input("Enter Username: ").lower()
    password = input("Enter Password: ").lower()
    with open("pswd.txt", "a") as pass_file:
        encrypted_password = fer.encrypt(password.encode()).decode()
        pass_file.write(f"{username}|{encrypted_password}\n")
        print("Password created")

def read_pass():
    key = load_key()
    fer = Fernet(key)
    with open("pswd.txt", "r") as read_pass_file:
        for line in read_pass_file:
            username, encrypted_password = line.strip().split("|")
            password = fer.decrypt(encrypted_password.encode()).decode()
            print(f"Username: {username} | Password: {password}")

option = input("add to Add Password | view to View Password | q to Quit: ")
if option == "add":
    write_pass()
elif option == "view":
    read_pass()
elif option == "q":
    print("Goodbye!")
else:
    print("Wrong Input")