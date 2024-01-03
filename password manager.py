import getpass

W = input("Welcome! You can save or view your passwords here.\nPress 'Enter' to proceed\n")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"User: {user}, Password: {passw}")

def add():
    name = input("Account Name: ")

    # Check if the username already exists
    if is_duplicate_username(name):
        print("Username already exists. Please choose a different one.")
        return

    pwd = getpass.getpass("Password: ")

    # Check if the password already exists
    if is_duplicate_password(pwd):
        print("Password already exists. Please choose a different one.")
        return

    with open('passwords.txt', 'a') as f:
        f.write(f"{name}|{pwd}\n")

def is_duplicate_username(username):
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            existing_user, _ = line.strip().split("|")
            if existing_user == username:
                return True
    return False

def is_duplicate_password(password):
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            _, existing_password = line.strip().split("|")
            if existing_password == password:
                return True
    return False

while True:
    mode = input("Would you like to enter a new password [add] or view existing ones [view]. Or press 'q' to quit!\n")
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue

