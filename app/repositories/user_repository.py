# CRUD Functions For All The Users
from pathlib import Path
import json

class UserRepository:

    def __init__(self) -> None:
        self.data_dir = Path("data")
        self.users_file = self.data_dir/"users.json"

        self._initialize_users_file()

    # Initialize User Database
    def _initialize_users_file(self):

        self.data_dir.mkdir(parents=True, exist_ok=True)

        if not self.users_file.exists():
            with self.users_file.open("w", encoding="utf-8") as file:
                json.dump({"users":[]}, file, indent= 4)

    # Add User In Database
    def add_user(self, name, email):

        # Get ID
        with self.users_file.open("r", encoding='utf-8') as file:
            data = json.load(file)
            users = data['users']

        if not self.verify_email(email):
            return

        max_id = 0
        if users:
            max_id = max(user['id'] for user in users)

        new_user = {
            "id": max_id + 1,
            "name": name,
            "email":email
        }

        # Check If User Is Already Present
        for user in users:
            if user['email'] == email:
                print("User Is Already Present In Database ")
                return

        # Add User In Database
        users.append(new_user)
        with self.users_file.open("w", encoding='utf-8') as file:
            json.dump(data, file, indent=4)
            print("New User Added Succesfully")

    # Search User
    def get_user(self, name = None, email = None):

        if name is not None and email is not None:
            print("Please Provide Either Name Or Email, Not Both")
            return
        elif name is None and email is None:
            print("Please Provide Either Name Or Email")
            return

        with self.users_file.open("r", encoding='utf-8') as file:
            data = json.load(file)
            users = data["users"]

        if name is not None:
            result = [
                user for user in users
                if user['name'].lower() == name.lower()
            ]
        else:
            result = [
                user for user in users
                if user['email'].lower() == email.lower()
            ]

        return result


    # Update User In Database
    def update_user(self, id, name = None, email = None):

        # Get Users
        with self.users_file.open("r", encoding='utf-8') as file:
            data = json.load(file)
            users = data["users"]
        for user in users:
            if user["id"] == id:
                if email is not None:
                    if self.verify_email(email):
                        user["email"] = email
                if name is not None:
                    user["name"] = name
                print("User updated Succesfully")

        with self.users_file.open("w", encoding='utf-8') as file:
            json.dump(data, file, indent= 4)
        return

        # Check email is unique
    def verify_email(self, email) -> bool:

        with self.users_file.open('r', encoding='utf-8') as file:
            data = json.load(file)
            users = data['users']

        for user in users:
            if user['email'] == email:
                print("Email already exist")
                return False

        return True

    # Delete User
    def delete_user(self, id):
        # Load all the users
        with self.users_file.open("r", encoding='utf-8') as file:
            data = json.load(file)
            users = data['users']

        target_user = None
        for user in users:
            if user['id'] == id:
                target_user = user

        if target_user is None:
            print("User not found")
            return
        else:
            users.remove(target_user)
            print("User deleted Succesfully")

        with self.users_file.open("w", encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        return

    


