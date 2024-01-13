import time
from extras import Extras
from registration import PlayerRegistration
from leaderBoard import LeaderBoard
from datetime import datetime, timezone
from tasks import Task
import calendar
from colorama import init
from colorama import Fore
init()


class GamePlay:
    def __init__(self):
        self.player_points = 0
        self.player_health = 5
        self.player_position = "outside_castle"
        self.guard_1 = True
        self.has_red_key = False
        self.has_green_key = False
        self.dog = True
        self.red_chest_unlocked = False
        self.red_chest_open = False
        self.green_door_unlocked = False
        self.has_armor = False
        self.has_adv_weapon = False
        self.has_health_potion = False
        self.c_c_pots = 2
        self.mid_c_pots = 3
        self.game_status = False
        self.slow = Extras()
        self.login = PlayerRegistration()
        self.username = ""
        self.leader_board = LeaderBoard()
        self.char_name = ""
        self.main_task = Task()

    def game_play(self):
        try:
            self.username = self.login.login()
            self.slow.slow_print("""
                1. Start a new game
                2. Load last saved
                3. Exit
                """)
            while True:
                print(Fore.CYAN)
                gamer_selection = input("Enter the index of your choice: ")

                if gamer_selection == "1":
                    self.starting_prompt()
                    exit()
                elif gamer_selection == "2":
                    self.load_game(self.username)
                    exit()
                elif gamer_selection == "3":
                    exit()
                else:
                    self.slow.slow_print("""
                    Invalid Input, Please choose from the above options.
                             """)
        except Exception as error:
            self.slow.slow_print(error)

    def starting_prompt(self):
        self.slow.slow_print(Fore.GREEN + """
            You are standing at the front of the castle. You have a rusty sword, it wont defeat the
            the boss but it'll do the trick against his guards. The castle has a door, it is open but
            a Guard stands in your way. Careful with your health, if it falls to 0, you lose the game.

            HINT: You can give commands to your avatar, try to use simple action words, e.g, if you want
            your avatar to enter a through a door to a room, give the command 'enter'. You can enter help
            to show you a list of commands if you get confused.
            """)
        # make command to lower and split function
        try:
            while True:
                command = input(Fore.CYAN + "Gamer command: ")
                command = command.lower()
                if command == 'smash' or command == 'unlock' or command == 'open' or command == 'take':
                    self.slow.slow_print(Fore.GREEN + f"""
            There is nothing to {command} here.
                        """)
                elif command == 'help':
                    self.slow.help()
                elif command == 'i' or command == 'inventory':
                    self.slow.inventory(self.has_armor, self.has_adv_weapon, self.has_health_potion,
                                        self.has_green_key, self.has_red_key)
                elif command == 'enter':
                    if self.guard_1:
                        self.slow.slow_print(Fore.GREEN + """
            You can not enter the castle, the guard is in your way. Defeat him in order to proceed.
                        """)
                    else:
                        break
                elif command == 'attack' and self.guard_1:
                    self.player_points = self.player_points + 10  # update points, store in file
                    self.player_health = self.player_health - 1  # update health, store in file
                    self.guard_1 = False
                    self.slow.slow_print(Fore.GREEN + f"""
            The guard is defeated. Your health reduced during combat. Your health is {self.player_health}
                        """)
                elif command == 'attack' and not self.guard_1:
                    self.slow.slow_print(Fore.GREEN + """
            The guard is already defeated. You can enter the castle.
                        """)
                elif command.lower() == 'exit':
                    exit()
                else:
                    self.slow.slow_print(Fore.GREEN + """
            Invalid command, try again.
                        """)
            self.slow.slow_print(Fore.GREEN + """
            You have entered the castle.
                        """)
            self.player_position = "common_chamber"
            self.save_game()
            self.common_chamber()
        except Exception as error:
            self.slow.slow_print(error)

    def common_chamber(self):
        self.slow.slow_print(Fore.GREEN + """
            Now you are in the Common chamber.
            There is a table next to you in this room, with two keys lying on it. One key is Green and the other is Red.
            There is a Green door in front of you which leads to the Middle Chamber. You can unlock the door with one of
            the keys. There is a pot here, it seems breakable, you can smash it with your sword.

            Type "enter" to enter the chamber or type "take" to take the keys.
            Warning: You might not be able to win the game without the keys.
            """)
        ask_key_to_take = False
        ask_key_to_unlock = False
        try:
            while True:
                command = input(Fore.CYAN + "Gamer command: ")
                command = command.lower()
                if (command == 'attack' or command == 'open') and not ask_key_to_take and not ask_key_to_unlock:
                    self.slow.slow_print(Fore.GREEN + f"""
            There is nothing to {command} here.
                        """)
                elif command == 'help' and not ask_key_to_take and not ask_key_to_unlock:
                    self.slow.help()
                elif command == 'smash' and not ask_key_to_take and not ask_key_to_unlock:
                    if self.c_c_pots > 0:
                        self.c_c_pots = self.c_c_pots - 1
                        self.player_points = self.player_points + 10
                        self.slow.slow_print(Fore.GREEN + f"""
            You smashed the pot. Your score increased to {self.player_points} 
                        """)
                    else:
                        self.slow.slow_print(Fore.GREEN + """
            There is nothing to smash here.
                            """)
                elif command == 'i' and not ask_key_to_take and not ask_key_to_unlock:
                    self.slow.inventory(self.has_armor, self.has_adv_weapon, self.has_health_potion,
                                        self.has_green_key, self.has_red_key)
                elif command == 'unlock' and not ask_key_to_take:
                    if not self.has_red_key and not self.has_green_key:
                        self.slow.slow_print(Fore.GREEN + """
            You do not have any key to unlock it with.
                        """)
                    elif not self.green_door_unlocked:
                        ask_key_to_unlock = True
                        self.slow.slow_print(Fore.GREEN + """
            Which key do you want to use ?
                        """)
                    else:
                        self.slow.slow_print(Fore.GREEN + """
            The door is already unlocked.
                        """)
                elif command == 'red' and ask_key_to_unlock:
                    ask_key_to_unlock = False
                    self.slow.slow_print(Fore.GREEN + """
            The Red key does not unlock the Green door. Nothing happens. 
                        """)
                elif command == 'green' and ask_key_to_unlock:
                    ask_key_to_unlock = False
                    if self.has_green_key:
                        self.green_door_unlocked = True
                        self.slow.slow_print(Fore.GREEN + """
            The Green door unlocks, you can now enter the Middle Chamber.
                        """)
                    else:
                        self.slow.slow_print(Fore.GREEN + """
            You do not have the Green key. Nothing happens.
                        """)
                elif command == "enter" and not ask_key_to_take and not ask_key_to_unlock:
                    if self.green_door_unlocked:
                        break
                    else:
                        self.slow.slow_print(Fore.GREEN + """
            The Green door is locked. You can not enter the Middle Chamber.
                        """)
                elif command == 'take' and not ask_key_to_unlock:
                    ask_key_to_unlock = False
                    if self.has_red_key and self.has_green_key:
                        self.slow.slow_print(Fore.GREEN + """
            There is nothing here to take.
                        """)
                    else:
                        ask_key_to_take = True
                        self.slow.slow_print(Fore.GREEN + """
            Which key do you want to take ?
                        """)
                elif command == 'red' and ask_key_to_take:
                    ask_key_to_take = False
                    if self.has_red_key:
                        self.slow.slow_print(Fore.GREEN + """
            You already have the Red key.    
                        """)
                    else:
                        self.has_red_key = True
                        self.slow.slow_print(Fore.GREEN + """
            You have taken the Red key.
                        """)
                elif command == 'green' and ask_key_to_take:
                    ask_key_to_take = False
                    if self.has_green_key:
                        self.slow.slow_print(Fore.GREEN + """
            You already have the Green key.    
                        """)
                    else:
                        self.has_green_key = True
                        self.slow.slow_print(Fore.GREEN + """
            You have taken the Green key.
                        """)
                elif command == 'exit' and not ask_key_to_take and not ask_key_to_unlock:
                    exit()
                else:
                    ask_key_to_take = False
                    ask_key_to_unlock = False
                    self.slow.slow_print(Fore.GREEN + """
            Invalid input, try again.    
                        """)
            self.player_position = "middle_chamber"
            self.save_game()
            self.middle_chamber()
            # Changes made here, cut out Door unlocked, player position
            # should be discussed
        except Exception as error:
            self.slow.slow_print(error)

    def middle_chamber(self):
        self.slow.slow_print(Fore.GREEN + """
            You are standing in the Middle Chamber.
            There is a red chest here guarded by a dog.
            There is a door after the chest leading to the Main Chamber. The door is unlocked, but you might
            find something useful in the chest.
        """)
        ask_red_key = False
        try:
            while True:
                command = input(Fore.CYAN + "Gamer command: ")
                command = command.lower()
                if command == 'smash' and not ask_red_key:
                    if self.mid_c_pots > 0:
                        self.mid_c_pots = self.mid_c_pots - 1
                        self.player_points = self.player_points + 10
                        self.slow.slow_print(Fore.GREEN + f"""
                    You smashed the pot. Your score increased to {self.player_points} 
                                """)
                    else:
                        self.slow.slow_print(Fore.GREEN + """
                    There is nothing to smash here.
                                    """)
                elif command == 'help' and not ask_red_key:
                    self.slow.help()
                elif command == 'i' and not ask_red_key:
                    self.slow.inventory(self.has_armor, self.has_adv_weapon, self.has_health_potion,
                                        self.has_green_key, self.has_red_key)
                elif command == 'enter' and not ask_red_key:
                    break
                elif command == 'attack' and not ask_red_key:
                    if self.dog:
                        if self.player_health == 1:
                            self.slayed_by_dog()
                            break
                        else:
                            self.dog = False
                            self.player_points = self.player_points + 10
                            self.player_health = self.player_health - 1
                            self.slow.slow_print(Fore.GREEN + f"""
            You defeated the dog, your health reduced during combat. You can now unlock the chest.
            Your health is {self.player_health}
                        """)
                    else:
                        ask_red_key = False
                        self.slow.slow_print(Fore.GREEN + """
            The dog has already been defeated.
                        """)
                elif command == 'unlock':
                    if self.dog:
                        if self.player_health == 1:
                            self.slayed_by_dog()
                            break
                        else:
                            self.player_health = self.player_health - 1
                            self.slow.slow_print(Fore.GREEN + f"""
            The dog bit you and you lost health, you can not unlock the chest without defeating the dog.
            Your health is {self.player_health} 
                        """)
                    elif self.red_chest_unlocked:
                        self.slow.slow_print(Fore.GREEN + """
            The red chest is already unlocked.
                        """)
                    else:
                        self.slow.slow_print(Fore.GREEN + """
            Which key do you want to use ?
                        """)
                        ask_red_key = True
                elif command == 'red' and ask_red_key:
                    ask_red_key = False
                    if self.has_red_key:
                        self.red_chest_unlocked = True
                        self.slow.slow_print(Fore.GREEN + """
            You used the red key to unlock the red chest. You can now open it.
                        """)
                    else:
                        self.slow.slow_print(Fore.GREEN + """
            Oops, looks like you dont have the red key. Nothing happens.
                        """)
                elif command == 'green' and ask_red_key:
                    ask_red_key = False
                    self.slow.slow_print(Fore.GREEN + """
            The green key does not unlock the red chest. Nothing happens.
                        """)
                elif command == 'open' and not ask_red_key:
                    if self.red_chest_unlocked and not self.red_chest_open:
                        self.red_chest_open = True
                        self.slow.slow_print(Fore.GREEN + """
            You open the chest and find a piece of Armor. You can take the Armor.
                        """)
                    elif self.dog:
                        if self.player_health == 1:
                            self.slayed_by_dog()
                            break
                        else:
                            self.player_health = self.player_health - 1
                            self.slow.slow_print(Fore.GREEN + f"""
            The dog bit you and you lost health, you can not open the chest without defeating the dog.
            Your health is {self.player_health}
                        """)
                    elif self.red_chest_open:
                        self.slow.slow_print(Fore.GREEN + """
            It is already open.
                        """)
                    elif not self.red_chest_unlocked:
                        self.slow.slow_print(Fore.GREEN + """
            The chest is locked, you can unlock it with a key.
                        """)
                elif command == 'take' and not ask_red_key:
                    if self.red_chest_open:
                        if self.has_armor:
                            self.slow.slow_print(Fore.GREEN + """
            There is nothing here to take.
                        """)
                        else:
                            self.has_armor = True
                            self.slow.slow_print(Fore.GREEN + """
            You have taken and worn the Armor. It will help you to defeat the Boss.
                        """)
                    else:
                        self.slow.slow_print(Fore.GREEN + """
            There is nothing here to take.
                        """)
                elif command == 'exit' and not ask_red_key:
                    exit()
                else:
                    ask_red_key = False
                    self.slow.slow_print(Fore.GREEN + """
            Invalid command, try again.
                        """)
            self.player_position = "main_chamber"
            self.save_game()
            self.main_chamber()
        except Exception as error:
            self.slow.slow_print(error)

    def main_chamber(self):
        self.main_task.task_1(self.username, self.char_name, self.player_points, self.player_health, self.game_status)
        self.has_adv_weapon = True
        self.main_task.task_2(self.username, self.player_points, self.player_health, self.game_status)
        self.has_health_potion = True
        try:
            while True:
                command = input(Fore.CYAN + "Gamer command: ")
                command = command.lower()
                if command == 'smash' or command == 'unlock' or command == 'open' or command == 'take':
                    self.slow.slow_print(Fore.GREEN + f"""
            There is nothing to {command} here.
                            """)
                elif command == 'help':
                    self.slow.help()
                elif command == 'i':
                    self.slow.inventory(self.has_armor, self.has_adv_weapon, self.has_health_potion,
                                        self.has_green_key, self.has_red_key)
                elif command == 'enter':
                    break
                else:
                    self.slow.slow_print(Fore.GREEN + """
            Invalid command, try again.
                        """)

            self.player_position = "boss_chamber"
            self.boss_chamber()
        except Exception as error:
            self.slow.slow_print(error)

    def boss_chamber(self):
        self.slow.slow_print(Fore.GREEN + """
            You have entered the Boss Chamber. He faces you and awaits your attack. Careful, you only have
            one chance and cant defeat him without full health. You can heal with your health potion.
                    """)
        try:
            while True:
                command = input(Fore.CYAN + "Gamer command: ")
                command = command.lower()
                if command == 'smash' or command == 'unlock' or command == 'open' or command == 'take':
                    self.slow.slow_print(Fore.GREEN + f"""
            There is nothing to {command} here.
                                """)
                elif command == 'help':
                    self.slow.help()
                elif command == 'i' or command == 'inventory':
                    self.slow.inventory(self.has_armor, self.has_adv_weapon, self.has_health_potion,
                                        self.has_green_key, self.has_red_key)
                elif command == 'heal':
                    if self.player_health < 10:
                        self.player_health = 10
                        self.slow.slow_print(Fore.GREEN + """
            You have used the health potion and healed to full health !
                        """)
                    else:
                        self.slow.slow_print(Fore.GREEN + """
            You have full health.
                        """)
                elif command == 'attack':
                    if self.has_armor and self.has_adv_weapon and self.player_health == 10:
                        self.slow.slow_print(Fore.GREEN + """
            HOORAY! You have defeated the boss.
                        """)
                        self.game_status = True
                        self.leader_board.leader_board(self.username, self.player_health, self.player_points,
                                                       self.game_status)
                        exit()
                    else:
                        self.slow.slow_print(Fore.RED + """
            The Boss has defeated you. Now no one can save the princess.        
                        """)
                        self.leader_board.leader_board(self.username, self.player_health, self.player_points,
                                                       self.game_status)
                        break
                elif command.lower() == 'exit':
                    exit()

        except Exception as error:
            self.slow.slow_print(error)

    def load_game(self, username):
        self.slow.slow_print("""
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
            self.has_red_key = bool(user_list[-1][-2].strip())
            self.has_green_key = bool(user_list[-1][-3].strip())
            self.player_position = user_list[-1][-4].strip()
            self.player_health = int(user_list[-1][-5].strip())
            self.player_points = int(user_list[-1][-6].strip())

            if self.player_position == "common_chamber":
                self.common_chamber()
            elif self.player_position == "middle_chamber":
                self.middle_chamber()
            else:
                self.main_chamber()
        else:
            print(f"{username} not found.")

    def save_game(self):
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

        self.slow.slow_print(Fore.CYAN + """
        You can save the at this stage!
        Do you want to save?(Y/N)""")
        while True:
            choice = input("Enter your choice: ")
            if choice.upper() == "Y":
                with open("../resources/gameProgress.txt", "a") as file:
                    file.write(f"{self.username}:{self.char_name}:{self.player_points}:"
                               f"{self.player_health}:{self.player_position}:{self.has_red_key}:{self.has_green_key}:"
                               f"{formatted_time}\n")
                self.slow.slow_print("""
                The game has been saved successfully.
                Do you want to continue playing?
                You can either type "continue" or "end".""")
                choice_1 = input("Gamer command: ")
                if choice_1.upper() == "CONTINUE":
                    break
                elif choice_1.upper() == "END":
                    self.slow.slow_print("""
                    Game closed.
                    You can reload your progress just by logging in to the game.""")
                    quit()
                else:
                    self.slow.slow_print("""
                    Invalid input. please enter either "continue" or "end".
                    """)
            elif choice.upper() == "N":
                self.slow.slow_print("""
                Ok!
                Lets continue the game.""")
                break

    def slayed_by_dog(self):
        self.slow.slow_print(Fore.RED + """
                    You have been slayed by the dog, you lose.
        =====================GAME OVER=======================
                                """)
        self.leader_board.leader_board(self.username, self.player_health, self.player_points,
                                       self.game_status)
        exit()
