from extras import Extras
from getpass4 import getpass

class PlayerRegistration:
        def __init__(self):
            self.slow = Extras()
            self.username = ""
            self.selectedCharacter = ""
        def welcomePage(self):
            self.slow.slowPrint("\n1. Register\n2. Login\n3. Quit")
            while True:
                choice = input("\nEnter your choice: ")
                if choice == '1':
                    self.registerAndCharCreate()
                    break
                elif choice == '2':
                    break
                elif choice == '3':
                    exit()
                else:
                    self.slow.slowPrint("Invalid input. Please try again.")

        def login(self):
            while True:
                # login
                self.username = input("Enter your username: ")
                password = getpass("Enter your password : ")

                with open("../resources/userDetails.txt", "r") as file:
                    login_successful = False
                    for line in file:
                        if ":" in line:
                            user, pwd = line.strip().split(":", 1)
                            if user == self.username and pwd == password:
                                self.slow.slowPrint("Login successful!")
                                login_successful = True
                                break  # Break the loop if login is successful

                    if login_successful:
                        return self.username
                    else:
                        self.slow.slowPrint("Invalid username or password.")
                        retry_option = input("Enter '1' to retry or '2' to register: ")
                        if retry_option == '2':
                            self.registerAndCharCreate()
                        elif retry_option != '1':
                            self.slow.slowPrint("Invalid option.")
                            self.welcomePage()
                            break

        def registerAndCharCreate(self):
            #Registration
            self.username = input("Enter a username: ")

            with open("../resources/userDetails.txt", "r") as file:
                lines = file.readlines()
                users = [line.split(":")[0] for line in lines]
            i = "y"
            while self.username in users and i == "y":
                self.slow.slowPrint("Username already exists.")
                i = input("Do you want to try again? (y/n)\n")

                while i != "y" and i != "n":
                    self.slow.slowPrint("Invalid input. Try again.")
                    i = input("Do you want to try again? (y/n)\n")

                if i == "y":
                    self.username = input("Enter your username: ")
                elif i == "n":
                    break

            if i == "y":
                password = getpass("Enter a password(Min length 5): ")
                while len(password) <5:
                    password = getpass("Password length must be minimum 5, please retry: ")
            else:
                self.welcomePage()

            self.slow.slowPrint("Registration successful!\nCreate your character.\n")
            with open("../resources/userDetails.txt", "a") as file:
                file.write(f"{self.username}:{password}\n")

            #Character creation
            selection = False
            while selection == False:
                charSex = input("What is your character's gender(M/F): ")
                if charSex == "M" or charSex == "F" or charSex == "m" or charSex == "f":
                    self.slow.slowPrint("\nGender has been selected!")
                    selection = True
                else:
                    self.slow.slowPrint("\nInvalid input, try again.\n")
                if selection:
                    break

            characterList = ['Knight 1', 'Knight 2', 'Knight 3', 'Knight 4']

            self.slow.slowPrint("\nSelect a character from the below list.\n")
            while True:
                for i, character in enumerate(characterList, start=1):
                    print(f"{i}. {character}")
                try:
                    characterSelection = int(input("Enter the index of your choice: "))
                    if 1 <= characterSelection <= len(characterList):
                        self.selectedCharacter = characterList[characterSelection - 1]
                        self.slow.slowPrint(f"Character '{self.selectedCharacter}' selected for {self.username}")
                        break
                    else:
                        self.slow.slowPrint("\nInvalid index. Please select a valid character index.\n")
                except ValueError:
                    self.slow.slowPrint("\nInvalid input. Please enter a number.")
            with open("../resources/charDetails.txt", "a") as file:
                file.write(f"{self.username}:{charSex}:{self.selectedCharacter}\n")
            self.slow.slowPrint("\nYour character creation is completed.\nNow login and dive into the game of adventures!\n")

