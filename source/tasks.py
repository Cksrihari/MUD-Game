from extras import Extras
from leaderBoard import LeaderBoard
from colorama import init
from colorama import Fore
init()


class Task:
    def __init__(self):
        self.slow = Extras()
        self.leader_board = LeaderBoard()
        self.nord_weapon = "Long Sword"
        self.elf_weapon = "Elven Bow"
        self.orc_weapon = "Heavy Mace"
        self.dwarf_weapon = "Broad Axe"

    def task_1(self, username, race, player_points, player_health, game_status):
        self.slow.slow_print(Fore.GREEN + """
        You are now in the Main Chamber. The door is locked!
        You have to complete two riddled to open the door and move forward.
        Here comes the first riddle!

        Riddle: I have a face but no eyes, hands but no arms,
                A tick-tock sound, yet do no harm.
                What am I?
                    """)

        chance = 2
        while True:
            self.slow.slow_print(Fore.GREEN + f"""
        Chances Left: {chance}
                    """)
            answer_task_1 = input(Fore.CYAN + """
        Options:
                a) Clock
                b) Statue
                c) Painting
                d) Mirror
        Answer: 
            """)

            if answer_task_1.upper() == "A":
                if race == 'Nord':
                    self.slow.slow_print(Fore.GREEN + f"""
        Genius! As you are a {race}, you have been awarded the {self.nord_weapon}.
        It'll help you to beat the Boss.
            """)
                elif race == 'Elf':
                    self.slow.slow_print(Fore.GREEN + f"""
        Genius! As you are a {race}, you have been awarded the {self.elf_weapon}.
        It'll help you to beat the Boss.
            """)
                elif race == 'Orc':
                    self.slow.slow_print(Fore.GREEN + f"""
        Genius! As you are a {race}, you have been awarded the {self.orc_weapon}.
        It'll help you to beat the Boss.
            """)
                else:
                    self.slow.slow_print(Fore.GREEN + f"""
        Genius! As you are a {race}, you have been awarded the {self.dwarf_weapon}.
        It'll help you to beat the Boss.
            """)
                    break
            elif answer_task_1.upper() in ["B", "C", "D"]:
                chance -= 1
                if chance > 0:
                    self.slow.slow_print(Fore.GREEN + """
        Oops! 
        Think harder. You have another chance.
        But this will be the last.
                    """)
                elif chance == 0:
                    self.slow.slow_print(Fore.RED + """
        You have lost the final chance. 
        You were unable to solve the riddle. 

=====================GAME OVER=======================
                    """)
                    self.leader_board.leader_board(username, player_points, player_health, game_status)
                    exit()
            else:
                self.slow.slow_print(Fore.GREEN + """
        Please choose from above options only.
                    """)

    def task_2(self, username, player_points, player_health, game_status):
        self.slow.slow_print(Fore.GREEN + """
        Continue thinking hard. 
        This is the last one!

        Riddle: I'm shiny and bright, but not made of gold,
                I turn and twist, yet in place I hold.
                What am I?        
                    """)

        chance = 2
        while True:
            self.slow.slow_print(Fore.CYAN + f"""
        Chances Left: {chance}
                    """)
            answer_task_2 = input("""
        Options:
                a) Sword
                b) Shield
                c) Crown
                d) Armor
        Answer: 
            """)

            if answer_task_2.upper() == "A":
                self.slow.slow_print(Fore.GREEN + """
        Genius! You have been awarded a health potion, use it wisely.
        Now you can enter the Boss Chamber.
                    """)
                break
            elif answer_task_2.upper() in ["B", "C", "D"]:
                chance -= 1
                if chance > 0:
                    self.slow.slow_print(Fore.GREEN + """
        Oops! 
        Think harder. You have another chance.
        But this will be the last.
                    """)
                elif chance == 0:
                    self.slow.slow_print(Fore.RED + """
        You have lost the final chance. 
        You were unable to solve the riddle. 

=====================GAME OVER=======================
                    """)

                    self.leader_board.leader_board(username, player_points, player_health, game_status)
                    exit()
            else:
                self.slow.slow_print(Fore.GREEN + """
        Please choose from above options only.
                    """)
