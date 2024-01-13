from extras import Extras
from getpass4 import getpass


class PlayerRegistration:
        def __init__(self):
            self.slow = Extras()
            self.user_name = ""
            self.selected_character = ""
            self.char_sex = ""
            self.password = ""

        def welcome_page(self):
            self.slow.slow_print("\n1. Register\n2. Login\n3. Quit")
            while True:
                choice = input("\nEnter your choice: ")
                if choice == '1':
                    self.register_and_char_create()
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
                self.password = getpass("Enter your password : ")

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
                        return self.user_name
                    else:
                        self.slow.slow_print("Invalid username or password.")
                        retry_option = input("Enter '1' to retry or '2' to register: ")
                        if retry_option == '2':
                            self.register_and_char_create()
                        elif retry_option != '1':
                            self.slow.slow_print("Invalid option.")
                            self.welcome_page()
                            break

        def register_and_char_create(self):
            self.user_name = input("Enter a username: ")

            with open("../resources/userDetails.txt", "r") as file:
                lines = file.readlines()
                users = [line.split(":")[0] for line in lines]
            i = "y"
            while self.user_name in users and i == "y":
                self.slow.slow_print("Username already exists.")
                i = input("Do you want to try again? (y/n)\n")

                while i != "y" and i != "n":
                    self.slow.slow_print("Invalid input. Try again.")
                    i = input("Do you want to try again? (y/n)\n")

                if i == "y":
                    self.user_name = input("Enter your username: ")
                elif i == "n":
                    break

            if i == "y":
                self.password = getpass("Enter a password(Min length 5): ")
                while len(self.password) <5:
                    self.password = getpass("Password length must be minimum 5, please retry: ")
            else:
                self.welcome_page()

            self.slow.slow_print("Registration successful!\nCreate your character.\n")
            with open("../resources/userDetails.txt", "a") as file:
                file.write(f"{self.user_name}:{self.password}\n")

            #Character creation
            selection = False
            while not selection:
                self.char_sex = input("What is your character's gender(M/F): ")
                if self.char_sex.lower() == "m" or self.char_sex.lower() == "f":
                    self.slow.slow_print("\nGender has been selected!")
                    selection = True
                else:
                    self.slow.slow_print("\nInvalid input, try again.\n")
                if selection:
                    break

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
                    self.slow.slow_print("\nInvalid input. Please enter a number.")
            with open("../resources/charDetails.txt", "a") as file:
                file.write(f"{self.user_name}:{self.char_sex}:{self.selected_character}\n")
            self.slow.slow_print("""
            Your character creation is completed. 
            Now login and dive into the game of adventures!
            """)
