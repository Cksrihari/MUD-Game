from extras import Extras
import stdiomask


class PlayerRegistration:
    def __init__(self):
        self.slow = Extras()
        self.user_name = ""
        self.selected_character = ""
        self.char_sex = ""
        self.password = ""
        self.logged_in = False

    def welcome_page(self):
        self.slow.slow_print("\n1. Register\n2. Login\n3. Quit")
        while True:
            choice = input("\nEnter your choice: ")
            if choice == '1':
                self.register_add_username()
                self.register_add_pass()
                self.register_add_gender()
                self.register_select_character()
                break
            elif choice == '2':
                break
            elif choice == '3':
                exit()
            else:
                self.slow.slow_print("Invalid input. Please try again.")

    def login(self):
        while True:
            # login
            self.user_name = input("Enter your username: ")
            self.password = stdiomask.getpass("Enter your password : ", mask="*")

            with open("../resources/userDetails.txt", "r") as file:
                login_successful = False
                for line in file:
                    if ":" in line:
                        user, pwd = line.strip().split(":", 1)
                        if user == self.user_name and pwd == self.password:
                            self.slow.slow_print("Login successful!")
                            login_successful = True
                            break  # Break the loop if login is successful

                if login_successful:
                    self.logged_in = True
                    return self.user_name
                else:
                    self.slow.slow_print("""
Invalid username or password.
""")

    def register_add_username(self):
        while True:
            self.user_name = input("Enter a username: ")

            if len(self.user_name) <= 0:
                self.slow.slow_print("""
Username can not be blank
""")
                continue
            elif " " in self.user_name:
                self.slow.slow_print("""
You can not add blank spaces in the username.
""")
                continue

            # Load existing users only if the entered username is not blank or contains spaces
            with open("../resources/userDetails.txt", "r") as file:
                lines = file.readlines()
                users = [line.split(":")[0] for line in lines]

            if self.user_name in users:
                self.slow.slow_print("""
Username already exists.
""")
                self.welcome_page()
            elif self.user_name not in users:
                break

    def register_add_pass(self):

        while True:
            password = stdiomask.getpass("Enter a password (Min length 5): ", mask="*")
            if len(password) < 5:
                self.slow.slow_print("""
Password length must be minimum 5, please retry.
""")
                continue
            elif " " in password:
                self.slow.slow_print("""
Password cannot be blank or just spaces. Please retry.
""")
                continue
            elif len(password) >= 5:
                break
            else:
                self.welcome_page()

        self.slow.slow_print("Registration successful!\nCreate your character.\n")
        with open("../resources/userDetails.txt", "a") as file:
            file.write(f"{self.user_name}:{password}\n")

    def register_add_gender(self):
        selection = False
        while not selection:
            gender = input("What is your character's gender(M/F): ")
            if gender.lower() == "m":
                self.char_sex = "Male"
                self.slow.slow_print("\nGender has been selected!")
                selection = True
            elif gender.lower() == "f":
                self.char_sex = "Female"
                self.slow.slow_print("\nGender has been selected!")
                selection = True
            else:
                self.slow.slow_print("\nInvalid input, try again.\n")
            if selection:
                break

    def register_select_character(self):
        character_list = ['Nord', 'Elf', 'Orc', 'Dwarf']

        self.slow.slow_print("\nSelect a character from the below list.\n")
        while True:
            for i, character in enumerate(character_list, start=1):
                print(f"{i}. {character}")
            try:
                character_selection = int(input("Enter the index of your choice: "))
                if 1 <= character_selection <= len(character_list):
                    self.selected_character = character_list[character_selection - 1]
                    self.slow.slow_print(f"Character '{self.selected_character}' selected for {self.user_name}")
                    break
                else:
                    self.slow.slow_print("\nInvalid index. Please select a valid character index.\n")
            except ValueError:
                self.slow.slow_print("\nInvalid input. Please enter a number.\n")
        with open("../resources/charDetails.txt", "a") as file:
            file.write(f"{self.user_name}:{self.char_sex}:{self.selected_character}\n")
        self.slow.slow_print("""
            Your character creation is completed. 
            Now login and dive into the game of adventures!
""")
