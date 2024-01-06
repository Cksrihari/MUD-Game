from extras import Extras
class GamePlay:
    def __init__(self, player_points, health, has_mc_key, player_position):
        self.player_points = 0
        self.health = 1
        self.has_mc_key = False
        self.player_position = player_position
        self.slow = Extras()

    def gamePlay(self):
        self.slow.slowPrint("""
            1. Start a new game
            2. Load last saved
            3. Exit
            """)
        while True:
            gamerselection= input("Enter the index of your choice: ")
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
            You are standing at the front door of the castle. You have a rusty sword, it wont defeat the
            the boss but it'll do the trick against his guards. The door is open, you can enter the castle.
            What do you want to do ?""")
        command = input()
        try:
            while True:
                command = command.lower()
                command_array = command.split()
                # can use if "word" not in "command"
                if command_array[0] == 'enter' and command_array[1] == 'castle':
                    break
                else:
                    self.slow.slowPrint("Invalid command, try again.")
                    command = input()
        except:
            self.slow.slowPrint("An infinite loop exception has occurred")

    def common_chamber(self):
        self.slow.slowPrint("""
            You have entered the castle. You are standing in the Common Chamber.
            There are 3 doors on the side,
            door 1, door 2, door3, and one in the front leading to the Middle Chamber.
            What do you want to do ?""")
        command = input()
        try:
            while True:
                command = command.lower()
                command_array = command.split()
                if command_array[0] == 'enter' and command_array[1] == 'middle' and command_array[2] == 'chamber':
                    if self.has_mc_key == True:
                        break
                    else:
                        self.slow.slowPrint("""
                            The door is locked, it can only be opened with a key, which you do not possess.
                            Hint: The key is somewhere in the Common Chamber.
                            What do you want to do ?""")
                        command = input()
                elif command_array[0] == 'enter' and command_array[1] == 'door' and command_array[2] == '1':
                    self.slow.slowPrint("The door opens to a room, there is a guard in here. What do you want to do.")
                    command = input()
                    command = command.lower()
                    command_array = command.split()
                    if command_array[0] == 'attack' and command_array[1] == 'guard':
                        self.slow.slowPrint("Guard is defeated")
                        #Guard status will be updated
                        self.has_mc_key = True
                        self.player_points = self.player_points + 10
                        self.slow.slowPrint("""
                            The guard drops a key, you pick up the key and can now access the Middle Chamber.
                            What do you want to do ?""")
                        command = input()
                        command = command.lower()
                        command_array = command.split()
                        if command_array[0] == 'leave' and command_array == 'room':
                            self.slow.slowPrint("You are now in the Common Chamber. What do you want to do ?")
                            command = input()
                    else:
                        self.slow.slowPrint("Invalid command, try again.")
                        command = input()
                elif command_array[0] == 'enter' and command_array[1] == 'door' and command_array[2] == '2':
                    self.slow.slowPrint("""
                        You enter a room, there is a crystal in this room. You can pick it up.
                        What do you want to do ?""")
                    if command_array[0] == 'leave' and command_array == 'room':
                        self.slow.slowPrint("You are now in the Common Chamber. What do you want to do ?")
                        command = input()
                elif command_array[0] == 'enter' and command_array[1] == 'door' and command_array[2] == '3':
                    self.slow.slowPrint("""You enter a room, there is an orb inside.
                          But you must complete a riddle in order to obtain it.""")
                else:
                    self.slow.slowPrint("Invalid command, try again.")
                    command = input()
        except:
            self.slow.slowPrint("An infinite loop exception has occurred")