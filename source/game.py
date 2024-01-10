import time

from extras import Extras
from registration import PlayerRegistration
from leaderBoard import LeaderBoard
from datetime import datetime, timezone
from tasks import Task
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
        self.green_door_unlocked = False
        self.has_armor = False
        self.has_sharp_sword = False
        self.has_health_potion = False
        self.game_status = False
        self.slow = Extras()
        self.login = PlayerRegistration()
        self.username = ""
        self.leader_board = LeaderBoard()
        self.char_name = ""
        self.main_task = Task()

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
                self.saveGame()
                self.common_chamber()
                self.saveGame()
                self.middle_chamber()
                self.main_chamber()
                self.boss_chamber()
                self.game_status = True
                self.leader_board.leaderBoard(self.username, self.player_health, self.player_points, self.game_status)
            elif gamer_selection == "2":
                self.loadGame(self.username)
            elif gamer_selection == "3":
                exit()
            else:
                self.slow.slowPrint("""
                Invalid Input, Please choose from the above options.
                         """)

    def starting_prompt(self):
        self.slow.slowPrint("""
            You are standing at the front of the castle. You have a rusty sword, it wont defeat the
            the boss but it'll do the trick against his guards. The castle has a door, it is open but
            a Guard stands in your way.

            HINT: You can give commands to your avatar, try to use simple action words, e.g, if you want
            your avatar to enter a through a door to a room, give the command 'enter'. You can enter help
            to show you a list of commands if you get confused.
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
                    if command == 'help':
                        self.slow.help()
                    elif self.guard_1:
                        self.slow.slowPrint("""
            You can not enter the castle, the guard is in your way. Defeat him in order to proceed.
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
            self.slow.slowPrint("Exception occurred")

    def common_chamber(self):
        self.slow.slowPrint("""
            Now you are in the Common chamber.
            There is a table next to you in this room, with two keys lying on it. One key is green and the other is red.
            There is a Green door in front of you which leads to the Middle Chamber. You can unlock the door with one of
            the keys. There is a pot here, it seems breakable, you can smash it with your sword.

            Type "enter" to enter the chamber or type "take" to take the keys.
            Warning: You might not be able to win the game without the keys.
            """)
        ask_key_to_take = False
        ask_key_to_unlock = False
        pot = True
        try:
            while True:
                self.slow.slowPrint("""
            What do you want to do?
                        """)
                command = input("Gamer command: ")
                command = command.lower()
                if command == 'help':
                    self.slow.help()
                elif command == 'smash' and not ask_key_to_take and not ask_key_to_unlock:
                    if pot:
                        pot = False
                        self.player_points = self.player_points + 10
                        self.slow.slowPrint(f"""
            You smashed the pot. Your score increased to {self.player_points} 
                        """)
                    else:
                        self.slow.slowPrint("""
            There is nothing to smash here.
                            """)
                elif command == 'i' and not ask_key_to_take:
                    self.slow.slowPrint("""
            Display inventory, read from file.
                        """)
                elif command == 'unlock' and not ask_key_to_take:
                    if not self.has_red_key and not self.has_green_key:
                        self.slow.slowPrint("""
            You do not have any key to unlock it with.
                        """)
                    elif not self.green_door_unlocked:
                        ask_key_to_unlock = True
                        self.slow.slowPrint("""
            Which key do you want to use ?
                        """)
                    else:
                        self.slow.slowPrint("""
            The door already unlocked.
                        """)
                elif command == 'red' and ask_key_to_unlock:
                    ask_key_to_unlock = False
                    self.slow.slowPrint("""
            The red key does not unlock the Green door. Nothing happens. 
                        """)
                elif command == 'green' and ask_key_to_unlock:
                    ask_key_to_unlock = False
                    if self.has_green_key:
                        self.green_door_unlocked = True
                        self.slow.slowPrint("""
            The Green door unlocks, you can now enter the Middle Chamber.
                        """)
                    else:
                        self.slow.slowPrint("""
            You do not have the Green key. Nothing happens.
                        """)
                elif command == "enter" and not ask_key_to_take and not ask_key_to_unlock:
                    if self.green_door_unlocked:
                        break
                    else:
                        self.slow.slowPrint("""
            The Green door is locked. You can not enter the Middle Chamber.
                        """)
                elif command == 'take' and not ask_key_to_unlock:
                    ask_key_to_unlock = False
                    if self.has_red_key and self.has_green_key:
                        self.slow.slowPrint("""
            There is nothing here to take.
                        """)
                    else:
                        ask_key_to_take = True
                        self.slow.slowPrint("""
            Which key do you want to take
                        """)
                elif command == 'red' and ask_key_to_take:
                    ask_key_to_take = False
                    if self.has_red_key:
                        self.slow.slowPrint("""
            You already have the red key.    
                        """)
                    else:
                        self.has_red_key = True
                        self.slow.slowPrint("""
            You have taken the Red key.
                        """)
                elif command == 'green' and ask_key_to_take:
                    ask_key_to_take = False
                    if self.has_green_key:
                        self.slow.slowPrint("""
            You already have the Green key.    
                        """)
                    else:
                        self.has_green_key = True
                        self.slow.slowPrint("""
            You have taken the Green key.
                        """)
                else:
                    ask_key_to_take = False
                    ask_key_to_unlock = False
                    self.slow.slowPrint("""
            Invalid input. try again.    
                        """)
            self.player_position = "middle_chamber"  # Changes made here, cut out Door unlocked, player position
            # should be discussed
        except:
            self.slow.slowPrint("Exception occurred")

    def middle_chamber(self):
        self.slow.slowPrint("""
            You are standing in the Middle Chamber.
            There is a red chest here guarded by a dog.
            There is a door after the chest leading to the Main Chamber. The door is unlocked, but you might
            find something useful in the chest.
        """)
        ask_red_key = False
        try:
            while True:
                self.slow.slowPrint("""
            What do you want to do?
                        """)
                command = input("Gamer command: ")
                command = command.lower()
                if command == 'help':
                    self.slow.help()
                elif command == 'enter':
                    break  # discuss on whether enter without Armor
                elif command == 'attack':
                    if self.dog:
                        self.dog = False
                        self.player_points = self.player_points + 10
                        self.player_health = self.player_health - 1
                        self.slow.slowPrint("""
            You defeated the dog, your health reduced during combat. You can now unlock the chest.
                        """)
                    else:
                        ask_red_key = False
                        self.slow.slowPrint("""
            The dog has already been defeated.
                        """)
                elif command == 'unlock':
                    if self.dog:
                        self.slow.slowPrint("""
            The dog bit you, you can not unlock the chest without defeating the dog.
                        """)
                    elif self.red_chest_unlocked:
                        self.slow.slowPrint("""
            The red chest is already unlocked. You can open it.
                        """)
                    else:
                        self.slow.slowPrint("""
            Which key do you want to use ?
                        """)
                        ask_red_key = True
                elif command == 'red' and ask_red_key:
                    ask_red_key = False
                    if self.has_red_key:
                        self.red_chest_unlocked = True
                        self.slow.slowPrint("""
            You used the red key to unlock the red chest. You can now open it.
                        """)
                    else:
                        self.slow.slowPrint("""
            Oops, looks like you dont have the red key. Nothing happens.
                        """)
                elif command == 'green' and ask_red_key:
                    ask_red_key = False
                    self.slow.slowPrint("""
            The green key does not unlock the red chest. Nothing happens.
                        """)
                elif command == 'open':
                    if self.red_chest_unlocked and not self.red_chest_open:
                        self.red_chest_open = True
                        self.slow.slowPrint("""
            You open the chest and find a piece of Armor. You can take the Armor.
                        """)
                    elif self.dog:
                        self.slow.slowPrint("""
            The dog bit you, you can not open the chest without defeating the dog.
                        """)
                    elif self.red_chest_open:
                        self.slow.slowPrint("""
            It is already open.
                        """)
                    elif not self.red_chest_unlocked:
                        self.slow.slowPrint("""
            The chest is locked, you can unlock it with a key.
                        """)
                elif command == 'take' and self.red_chest_open:
                    if self.has_armor:
                        self.slow.slowPrint("""
            There is nothing here to take.
                        """)
                    else:
                        self.has_armor = True
                        self.slow.slowPrint("""
            You have taken and worn the Armor. It will help you to defeat the Boss.
                        """)
                else:
                    ask_red_key = False
                    self.slow.slowPrint("""
            Invalid command, try again.
                        """)
        except:
            self.slow.slowPrint("Exception occurred")

    def main_chamber(self):
        self.main_task.task_1()
        self.has_sharp_sword = True
        self.main_task.task_2()
        self.has_health_potion = True
        try:
            while True:
                command = input("Gamer command: ")
                command = command.lower()
                if command == 'help':
                    self.slow.help()
                elif command == 'enter':
                    break
                else:
                    self.slow.slowPrint("""
            Invalid command, try again.
                        """)
        except:
            self.slow.slowPrint("Exception occurred.")

    def boss_chamber(self):
        self.slow.slowPrint("""
            You have entered the Boss Chamber. He faces you and awaits your attack. Careful, you only have
            one chance and cant defeat him without full health. You can heal with your health potion.
                    """)
        try:
            while True:
                command = input("Gamer command: ")
                command = command.lower()
                if command == 'help':
                    self.slow.help()
                elif command == 'heal':
                    if self.player_health < 10:
                        self.player_health = 10
                        self.slow.slowPrint("""
                You have used the health potion and healed to full health !
                        """)
                    else:
                        self.slow.slowPrint("""
                You have full health.
                        """)
                elif command == 'attack':
                    if self.has_armor and self.has_sharp_sword and self.player_health == 10:
                        self.slow.slowPrint("""
                Hooray! You have defeated the boss.
                        """)
                        break
                else:
                    self.slow.slowPrint("""
                    The Boss has defeated you. Now no one can save the princess.        
                            """)
                    self.leader_board.leaderBoard(self.username, self.player_points, self.player_health,
                                                  self.game_status)
                    break
        except:
            self.slow.slowPrint("""
                Exception occurred.
                        """)

    def loadGame(self, username):
        self.slow.slowPrint("""
        Welcome back!
        """)
        game_progress = open("../resources/gameProgress.txt", "r")
        user_progress = game_progress.readlines()
        user_list = []
        for user in user_progress:
            user = user.split(":")
            if username == user[0]:
                user_list.append(user)
        if user_list:
            self.player_position = user_list[-1][-2].strip()
            self.player_points = int(user_list[-1][-4].strip())
            self.player_health = int(user_list[-1][-3].strip())

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
        user_list = []
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
