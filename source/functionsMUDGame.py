class functions_MUD:
        def welcomePage():
            print("\n1. Register\n2. Login\n3. Quit")
            choice = input("Enter your choice: ")

            if choice == '1':
                functions_MUD.register()
            elif choice == '2':
                functions_MUD.login()
            elif choice == '3':
                exit()
            else:
                print("Invalid input. Please try again.")

        def login():
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            with open("/Users/srihari/Documents/Application Programming/MUD Game Code/resources/userDetails.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    if ":" in line:
                        user, pwd = line.strip().split(":", 1)
                        if user == username and pwd == password:
                            print("Login successful!")
                            return
                        
            print("Invalid username or password")

        def register():
            username = input("Enter a username: ")

            with open("/Users/srihari/Documents/Application Programming/MUD Game Code/resources/userDetails.txt", "r") as file:
                lines = file.readlines()
                users = [line.split(":")[0] for line in lines]
            i = "y"
            while username in users and i == "y":
                print("Username already exists.")
                i = input("Do you want to try again? (y/n)\n")

                while i != "y" and i != "n":
                    print("Invalid input. Try again.")
                    i = input("Do you want to try again? (y/n)\n")

                if i == "y":
                    username = input("Enter your username: ")
                elif i == "n":
                    break

            if i == "y":
                password = input("Enter a password(Min length 5): ")
                while len(password) <5:
                    password = input("Password length must be minimum 5, please retry")
            else:
                functions_MUD.welcomePage()

            print("Registration successful!\nPlease Login to the game.\n")
            with open("/Users/srihari/Documents/Application Programming/MUD Game Code/resources/userDetails.txt", "a") as file:
                file.write(f"{username}:{password}\n")
            functions_MUD.login()

        def charCreate():
            charName = input("Choose your character name:\n")
            charSex = input("What if your character's gender:\n")
            charFaction = input("")
            
