from extras import extras
class playerRegistration:
        def __init__(self):
            self.slow = extras()

        def welcomePage(self):
            self.slow.slowPrint("\n1. Register\n2. Login\n3. Quit")
            while True:
                choice = input("\nEnter your choice: ")
                if choice == '1':
                    self.register()
                    break
                elif choice == '2':
                    self.login()
                    break
                elif choice == '3':
                    exit()
                else:
                    self.slow.slowPrint("Invalid input. Please try again.")

        def login(self):
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            with open("../resources/userDetails.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    if ":" in line:
                        user, pwd = line.strip().split(":", 1)
                        if user == username and pwd == password:
                            self.slow.slowPrint("Login successful!")
                            return
                        
            self.slow.slowPrint("Invalid username or password")

        def register(self):
            username = input("Enter a username: ")

            with open("../resources/userDetails.txt", "r") as file:
                lines = file.readlines()
                users = [line.split(":")[0] for line in lines]
            i = "y"
            while username in users and i == "y":
                self.slow.slowPrint("Username already exists.")
                i = input("Do you want to try again? (y/n)\n")

                while i != "y" and i != "n":
                    self.slow.slowPrint("Invalid input. Try again.")
                    i = input("Do you want to try again? (y/n)\n")

                if i == "y":
                    username = input("Enter your username: ")
                elif i == "n":
                    break

            if i == "y":
                password = input("Enter a password(Min length 5): ")
                while len(password) <5:
                    password = input("Password length must be minimum 5, please retry: ")
            else:
                self.welcomePage()

            self.slow.slowPrint("Registration successful!\nPlease Login to the game.\n")
            with open("../resources/userDetails.txt", "a") as file:
                file.write(f"{username}:{password}\n")
            self.login()

        def charCreate(self):
            charName = input("Choose your character name:\n")
            charSex = input("What if your character's gender:\n")
            charFaction = input("")
            
