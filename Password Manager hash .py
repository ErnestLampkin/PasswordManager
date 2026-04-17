# my pass manager with hashing and json for fair
import hashlib
import json
import os

FILE_NAME = "passwords.json"

def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except:
            return []
    return []

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

password_list = load_data()

def add_password():
    app = input("Enter app/website name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if app == "" or username == "" or password == "":
        print("Fields cannot be empty\n")
        return

    for entry in password_list:
        if entry["app"].lower() == app.lower():
            print("App already exists\n")
            return

    entry = {
        "app": app,
        "username": username,
        "password": hash_password(password)
    }

    password_list.append(entry)
    save_data(password_list)
    print("Password added\n")

def view_passwords():
    if len(password_list) == 0:
        print("No passwords\n")
        return

    for i, entry in enumerate(password_list):
        print(i + 1, entry["app"], entry["username"], entry["password"])
    print()

def search_password():
    app = input("Enter app name: ")

    for entry in password_list:
        if entry["app"].lower() == app.lower():
            print(entry["app"], entry["username"], entry["password"], "\n")
            return

    print("Not found\n")

def check_password():
    app = input("Enter app name: ")
    password = input("Enter password: ")

    for entry in password_list:
        if entry["app"].lower() == app.lower():
            if hash_password(password) == entry["password"]:
                print("Correct\n")
            else:
                print("Incorrect\n")
            return

    print("Not found\n")

def remove_password():
    app = input("Enter app name to remove: ")

    for i, entry in enumerate(password_list):
        if entry["app"].lower() == app.lower():
            password_list.pop(i)
            save_data(password_list)
            print("Removed\n")
            return

    print("Not found\n")

def edit_password():
    app = input("Enter app name to edit: ")

    for entry in password_list:
        if entry["app"].lower() == app.lower():
            new_username = input("Enter new username: ")
            new_password = input("Enter new password: ")

            if new_username == "" or new_password == "":
                print("Fields cannot be empty\n")
                return

            entry["username"] = new_username
            entry["password"] = hash_password(new_password)

            save_data(password_list)
            print("Updated\n")
            return

    print("Not found\n")

def main():
    while True:
        print("1 Add")
        print("2 View")
        print("3 Search")
        print("4 Check")
        print("5 Remove")
        print("6 Edit")
        print("7 Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            search_password()
        elif choice == "4":
            check_password()
        elif choice == "5":
            remove_password()
        elif choice == "6":
            edit_password()
        elif choice == "7":
            print("Goodbye")
            break
        else:
            print("Invalid choice\n")

main()
