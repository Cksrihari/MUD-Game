import time

from extras import Extras
from registration import PlayerRegistration
from leaderBoard import LeaderBoard
from datetime import datetime, timezone
import calendar

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
        self.login = PlayerRegistration()
        self.username = ""
        self.leader_board = LeaderBoard()
        self.char_name = ""
    def gamePlay(self):
        self.username = self.login.login()
        self.slow.slowPrint("""
            1. Start a new game
            2. Load last saved
            3. Exit
            """)
        while True:
            gamer_selection = input("Enter the index of your choice: ")
            if gamer_selection == "1":
                self.starting_prompt()
                #self.leader_board.leaderBoard(self.username, self.player_health, self.player_points)
                self.saveGame()
                self.common_chamber()
                self.saveGame()
                self.middle_chamber()
            elif gamer_selection == "2":
                self.loadGame(self.username)
            elif gamer_selection == "3":
                exit()
            else:
                self.slow.slowPrint("""
                Invalid Input, Please choose from the above options.""")

    def starting_prompt(self):
        self.slow.slowPrint("""
            You are standing at the front of the castle. You have a rusty sword, it wont defeat the
            the boss but it'll do the trick against his guards. The castle has a door, it is open but
            a Guard stands in your way.
            
            HINT: You can give commands to your avatar, try to use simple action words, e.g, if you want
            your avatar to enter a through a door to a room, give the command 'enter room'
            """)
          # make command to lower and split function
        try:
            while True:
                self.slow.slowPrint("""
                What do you want to do?
                """)
                command = input("Gamer command: ")
                command = command.lower()
                # can use if "word" not in "command"
                if command == 'enter':
                    if self.guard_1:
                        self.slow.slowPrint("""
                            You can not enter the castle, the guard is in your way. Defeat him in order to proceed.
                            What do you want to do ?
                        """)
                    else:
                        break

                elif command == 'attack' and self.guard_1:
                    self.player_points = self.player_points + 10  # update points, store in file
                    self.player_health = self.player_health - 1  # update health, store in file
                    self.guard_1 = False
                    self.slow.slowPrint("""
                        The guard is defeated. Your health reduced during combat.
                        """)

                elif command == 'attack' and not self.guard_1:
                    self.slow.slowPrint("""
                        The guard is already defeated. You can enter the castle.
                    """)
                else:
                    self.slow.slowPrint("""
                    Invalid command, try again.
                    """)
            self.slow.slowPrint("""
                You have entered the castle.
                """)
            self.player_position = "common_chamber"
        except:
            self.slow.slowPrint("An infinite loop exception has occurred")

    def common_chamber(self):
        self.slow.slowPrint("""
            Now you are in the common chamber.
            There is a table next to you in this room, with two keys lying on it. One key is green and the other is red.
            There is a door in front of you which leads to the Middle Chamber.
            
            Type "enter" to enter the chamber or type "pick" to pick the keys.
            Warning: You might not be able to complete the game without the keys.
            """)

        try:
            while True:
                command = input("Gamer command: ")
                if command == 'i':
                    self.slow.slowPrint("""
                        Display inventory, read from file.
                    """)
                elif command == "enter":
                    if self.has_red_key and self.has_green_key:
                        break
                    else:
                        self.slow.slowPrint("""
                        You need one of the keys to unlock the door to the middle chamber.
                        Try again once you are ready.""")

                elif command == 'pick':
                    self.has_red_key = True
                    self.has_green_key = True
                    self.slow.slowPrint("""
                    Good job!
                    You now possess a red key and a blue key.
                    """)
                else:
                    self.slow.slowPrint("""
                    Invalid input. try again.    
                    """)
            self.slow.slowPrint("""
            Door unlocked!""")
            self.player_position = "middle_chamber"
            ask_red_key = False
        except:
            self.slow.slowPrint("An infinite loop exception has occurred")



    def middle_chamber(self):


        self.slow.slowPrint("""
            You are standing in the Middle Chamber.
            There is a red chest here guarded by a dog.
            There is a door in front of you leading to the Main Chamber.
            What do you want to do ? 
        """)
        try:
            while True:
                command = input()
                command = command.lower()
                command_array = command.split()
                if command_array[0] == 'enter' or command_array == 'main' or command_array[2] == 'chamber':
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
        except:
            self.slow.slowPrint("An infinite loop exception has occurred")

    def loadGame(self, username):
        self.slow.slowPrint("""
        Welcome back!
        """)
        game_progress = open("../resources/gameProgress.txt", "r")
        user_progress = game_progress.readlines()
        user_list =[]
        for user in user_progress:
            user = user.split(":")
            if username == user[0]:
                user_list.append(user)
        if user_list:
            self.player_position = user_list[0][-2].strip()
            self.player_points = int(user_list[0][-4].strip())
            self.player_health = int(user_list[0][-3].strip())

            if self.player_position == "common_chamber":
                self.common_chamber()
            elif self.player_position == "middle_chamber":
                self.middle_chamber()
            else:
                print("call the function for main chamber")
        else:
            print(f"{username} not found.")



    def saveGame(self):
        current_GMT = time.gmtime()
        time_stamp = calendar.timegm(current_GMT)
        formatted_time = datetime.fromtimestamp(time_stamp, timezone.utc).strftime('%d/%m/%Y %H.%M.%S')
        data = open("../resources/charDetails.txt", "r")
        user_details = data.readlines()
        user_list =[]
        for user in user_details:
            user = user.split(":")
            if self.username == user[0]:
                user_list.append(user)
        self.char_name = user_list[0][-1].strip()

        self.slow.slowPrint("""
        You can save the at this stage!
        Do you want to save?(Y/N)""")
        while True:
            choice = input("Enter your choice: ")
            if choice.upper() == "Y":
                with open("../resources/gameProgress.txt", "a") as file:
                    file.write(f"{self.username}:{self.char_name}:{self.player_points}:"
                               f"{self.player_health}:{self.player_position}:{formatted_time}\n")
                self.slow.slowPrint("""
                The game has been saved successfully.
                Do you want to continue playing?
                You can either type "continue" or "end".""")
                choice_1 = input("Gamer command: ")
                if choice_1.upper() == "CONTINUE":
                    break
                elif choice_1.upper() == "END":
                    self.slow.slowPrint("""
                    Game closed.
                    You can reload your progress just by logging in to the game.""")
                    quit()
                else:
                    self.slow.slowPrint("""
                    Invalid input. please enter either "continue" or "end".
                    """)
            elif choice.upper() == "N":
                self.slow.slowPrint("""
                Ok!
                Lets continue the game.""")
                break