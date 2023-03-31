from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as file:
        file.write(key)

write_key()


def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)


def view():
    with open('password.txt', 'r') as file:
        for line in file.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| password:",
            fer.decrypt(passw.encode()).decode())
    

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as file:
        file.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    master_passwd = input("Input the master password: ")
    if master_passwd != "razaking113":
        print("invalid master password!")
        continue
    
    mode = input("would you like to view or add an existing password(view,add), press q to quit ? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()

    else:
        print("invalid keyword mode!")