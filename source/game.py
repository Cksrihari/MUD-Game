from extras import Extras


class GamePlay:
    def __init__(self):
        self.player_points = 0
        self.player_health = 10
        self.player_position = "outside_castle"
        self.guard_1 = True
        self.has_red_key = False
        self.has_green_key = False
        self.dog = True
        self.red_chest_unlocked = False
        self.red_chest_open = False
        self.has_armor = False
        self.slow = Extras()

    def gamePlay(self):
        self.slow.slowPrint("""
            1. Start a new game
            2. Load last saved
            3. Exit
            """)
        while True:
            gamerselection = input("Enter the index of your choice: ")
            if gamerselection == "1":
                self.starting_prompt()
            elif gamerselection == "2":
                print("have to add saving functions")
            elif gamerselection == "3":
                exit()
            else:
                self.slow.slowPrint("""
                
                Invalid Input, Please choose from the above options.""")

    def starting_prompt(self):
        self.slow.slowPrint("""
            You are standing at the front of the castle. You have a rusty sword, it wont defeat the
            the boss but it'll do the trick against his guards. The castle has a door, it is open but
            a Guard stands in your way.
            What do you want to do ?
            HINT: You can give commands to your avatar, try to use simple action words, e.g, if you want
            your avatar to enter a through a door to a room, give the command 'enter room'
            """)
        command = input()  # make command to lower and split function
        try:
            while True:
                command = command.lower()
                command_array = command.split()
                # can use if "word" not in "command"
                if command_array[0] == 'enter' and command_array[1] == 'castle' and self.guard_1 == False:
                    break
                elif command_array[0] == 'enter' and command_array[1] == 'castle' and self.guard_1 == True:
                    self.slow.slowPrint("""
                        You can not enter the castle, the guard is in your way. Defeat him in order to proceed.
                        What do you want to do ?
                    """)
                elif command_array[0] == 'attack' and command_array[1] == 'guard':
                    if self.guard_1:
                        self.player_points = self.player_points + 10  # update points, store in file
                        self.player_health = self.player_health - 1  # update health, store in file
                        self.guard_1 = False
                        self.slow.slowPrint("""
                            The guard is defeated. Your health reduced during combat. What do you want to do ?
                            """)
                    else:
                        self.slow.slowPrint("""
                            The guard is already defeated. What do you want to ?
                        """)
                else:
                    self.slow.slowPrint("""
                        Invalid command, try again.
                        """)
                command = input()
        except:
            self.slow.slowPrint("An infinite loop exception has occurred")

    def common_chamber(self):
        self.player_position = "common_chamber"
        self.slow.slowPrint("""
            You have entered the castle. You are standing in the Common Chamber.
            This is a safe zone, you can save your game here. 
            There is a table next to you in this room, with two keys lying on it. One key is green and the other is red.
            There is a door in front of you which leads to the Middle Chamber.
            What do you want to do ?""")
        command = input()
        try:
            while True:
                command = command.lower()
                command_array = command.split()
                if command_array[0] == 'save' or (command_array[0] == 'save' and command_array[1] == 'game'):
                    self.slow.slowPrint("""
                        Add functionality, Game saved. What do you want to do ?
                    """)  # save username, avatar, location, health, points, keys, weapon, orb, potion, timestamp
                elif command_array[0] == 'i':
                    self.slow.slowPrint("""
                        Display inventory, read from file.
                    """)
                elif command_array[0] == 'enter' and command_array[1] == 'middle' and command_array[2] == 'chamber':
                    break
                elif command_array[0] == 'take' and command_array[1] == 'red' and command_array[2] == 'key':
                    if not self.has_red_key:
                        self.has_red_key = True  # update inventory, store in file
                        self.slow.slowPrint("""
                            You have taken the red key. What do you want to do ?
                        """)
                    else:
                        self.slow.slowPrint("""
                            You have already taken the red key. What do you want to do ?
                        """)
                elif command_array[0] == 'take' and command_array[1] == 'green' and command_array[2] == 'key':
                    if not self.has_green_key:
                        self.has_green_key = True  # update inventory, store in file
                        self.slow.slowPrint("""
                            You have taken the green key. What do you want to do ?
                        """)
                    else:
                        self.slow.slowPrint("""
                            You have already taken the green key. What do you want to do ?
                        """)
                elif command_array[0] == 'take':
                    if self.has_red_key and self.has_green_key:
                        self.slow.slowPrint("""
                            There is nothing here to take.
                        """)
                    else:
                        self.slow.slowPrint("""
                            Take what ?
                        """)
                else:
                    self.slow.slowPrint("Invalid command, try again.")
                command = input()
        except:
            self.slow.slowPrint("An infinite loop exception has occurred")

    def middle_chamber(self):
        self.player_position = "middle_chamber"
        ask_red_key = False
        self.slow.slowPrint("""
            You are standing in the Middle Chamber. There is a red chest here guarded by a dog.
            There is a door in front of you leading to the Main Chamber.
            What do you want to do ? 
        """)
        command = input()
        try:
            while True:
                command = command.lower()
                command_array = command.split()
                if command_array[0] == 'enter' and command_array == 'main' and command_array[2] == 'chamber':
                    break
                elif command_array[0] == 'attack' and command_array[1] == 'dog':
                    if self.dog:
                        self.dog = False
                        self.player_points = self.player_points + 10
                        self.player_health = self.player_health - 1
                        self.slow.slowPrint("""
                            You defeated the dog, your health reduced during combat.
                            What do you want to do ?
                        """)
                    else:
                        ask_red_key = False
                        self.slow.slowPrint("""
                            The dog has already been defeated. What do you want to do ?
                        """)
                elif command_array[0] == 'unlock' and command_array[1] == 'red' and command_array[2] == 'chest':
                    if self.dog:
                        self.slow.slowPrint("""
                            The dog bit you, you can not unlock or open the chest without defeating the dog.
                            What do you want to do ?
                        """)
                    elif self.red_chest_unlocked:
                        self.slow.slowPrint("""
                            The red chest is already unlocked. What do you want to do ?
                        """)
                    else:
                        self.slow.slowPrint("""
                            Which key do you want to use ?
                        """)
                        ask_red_key = True
                elif command_array[0] == 'red' and command_array[1] == 'key' and ask_red_key:
                    ask_red_key = False
                    self.red_chest_unlocked = True
                    self.slow.slowPrint("""
                        You used the red key to unlock the red chest. What do you want to do ?
                    """)
                elif command_array[0] == 'green' and command_array[1] == 'key' and ask_red_key:
                    ask_red_key = False
                    self.slow.slowPrint("""
                        The green key does not unlock the red chest. Nothing happens.
                        What do you want to do ?
                    """)
                elif ((command_array[0] == 'open' and command_array[1] == 'chest') or
                      (command_array[0] == 'open' and command_array[1] == 'red' and command_array[2] == 'chest')):
                    if self.red_chest_unlocked:
                        self.red_chest_open = True
                        self.slow.slowPrint("""
                            You open the chest and find a piece of Armor. What do you want to do ?
                        """)
                    elif self.dog:
                        self.slow.slowPrint("""
                            The dog bit you, you can not unlock or open the chest without defeating the dog.
                            What do you want to do ?
                        """)
                    elif self.red_chest_open:
                        self.slow.slowPrint("""
                            It is already open. What do you want do ?
                        """)
                    elif not self.red_chest_unlocked:
                        self.slow.slowPrint("""
                            The chest is locked, you can open it with a key.
                            What do you want to do ?
                        """)
                elif command_array[0] == 'take' and command_array[1] == 'armor' and self.red_chest_open:
                    self.has_armor = True
                    self.slow.slowPrint("""
                        You have taken and worn the Armor. It will help you to defeat the Boss.
                        What do you want to do ?
                    """)
                else:
                    ask_red_key = False
                    self.slow.slowPrint("""
                        Invalid command, try again.
                    """)
                command = input()
        except:
            self.slow.slowPrint("An infinite loop exception has occurred")
