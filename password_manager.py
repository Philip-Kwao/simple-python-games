# This program is going to save usernames and passwords in specific file 
# Encrypts the password with a private key only known to the user 
from cryptography.fernet import Fernet 

def create_key():
    key=Fernet.generate_key() #Generating key for encyrption process
    with open("key.key", "wb") as key_file:
        key_file.write(key) #writing encryption key to file

def load_key():
    file=open("key.key","rb")
    key=file.read()
    file.close()
    return key

    

def write_pass():
    master_key = input("Master Key Value: ")
    key=load_key()
    fer= Fernet(key) + master_key

    with open("pswd.txt","a") as pass_file:
        username=input("Enter Username: ").lower()
        password=input("Enter Password: ").lower()
        encrypted_password=fer.encrypt(password.encode()).decode()
        pass_file.write(f"{username}|{encrypted_password}\n")

def read_pass():
    with open("pswd.txt", "r") as read_pass_file:
        pswd = read_pass_file.read()
        username, password= pswd.split("|")
        print(f"Username: {username} | Password: {password}")
    
option=input("add to Add Password | view to View Password | q to Quit: ")
if option == "add":
    write_pass()
elif option == "view":
    create_key()
elif option == "q":
    print("Goodbye!")
else:
    print("Wrong Input")