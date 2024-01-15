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
        self.chance = 2

    def task_1(self, username, race, player_points, player_health, game_status):
        self.slow.slow_print(Fore.GREEN + """
            You are now in the Main Chamber. The door to the Boss chamber is locked!
            You have to complete two riddles to open the door and move forward. Careful,
            there are only two chances for each riddle, and if you use them all up, a trap door
            will open sending you to your doom. Completing the riddles will grant you items
            that will help defeat the boss.

            Riddle: I have a face but no eyes, hands but no arms, a tick-tock sound, yet do no harm.
            What am I?
                        """)

        while True:
            self.slow.slow_print(Fore.GREEN + f"""
            Chances Left: {self.chance}
                        """)
            answer_task_1 = input(Fore.CYAN + """
            Options:
                a) Clock
                b) Statue
                c) Painting
                d) Mirror
            Answer: """)

            if answer_task_1.upper() == "A":
                self.slow.slow_print(Fore.GREEN + f"""
            Genius! As you are a {race}, you have been awarded the,
                        """)
                if race == 'Nord':
                    self.slow.slow_print(Fore.GREEN + f"""
                    {self.nord_weapon}
                        """)
                    break
                elif race == 'Elf':
                    self.slow.slow_print(Fore.GREEN + f"""
                    {self.elf_weapon}
                        """)
                    break
                elif race == 'Orc':
                    self.slow.slow_print(Fore.GREEN + f"""
                    {self.orc_weapon}   
                        """)
                    break
                else:
                    self.slow.slow_print(Fore.GREEN + f"""
                    {self.dwarf_weapon}
                        """)
                    break

            elif answer_task_1.upper() in ["B", "C", "D"]:
                self.chance -= 1
                if self.chance > 0:
                    self.slow.slow_print(Fore.GREEN + """
                    Oops! 
                    Think harder. You have another chance.
                    But this will be the last.
                                """)
                else:
                    self.slow.slow_print(Fore.RED + """
                    You have lost the final chance. You were unable to solve the riddle and fall to your doom. 
    
            =====================GAME OVER=======================
                                """)
                    self.leader_board.leader_board(username, player_points, player_health, game_status)
                    raise SystemExit
            else:
                self.slow.slow_print(Fore.GREEN + """
                        Please choose from the above options only.
                                    """)
            self.slow.slow_print(Fore.GREEN + """
        It'll help you to beat the Boss.
                    """)

    def task_2(self, username, player_points, player_health, game_status):
        self.slow.slow_print(Fore.GREEN + """
            Continue thinking hard. 
            This is the last one!

            Riddle: I'm shiny and bright, but not made of gold, I turn and twist, yet in place I hold.
            What am I?        
                        """)

        self.chance = 2
        try:
            while True:
                self.slow.slow_print(Fore.CYAN + f"""
                Chances Left: {self.chance}
                            """)
                answer_task_2 = input("""
                Options:
                    a) Sword
                    b) Shield
                    c) Crown
                    d) Armor
                Answer: """)

                if answer_task_2.upper() == "A":
                    self.slow.slow_print(Fore.GREEN + """
            Genius! You have been awarded a health potion, use it wisely.
            Now you can enter the Boss Chamber.
                        """)
                    break
                elif answer_task_2.upper() in ["B", "C", "D"]:
                    self.chance -= 1
                    if self.chance > 0:
                        self.slow.slow_print(Fore.GREEN + """
            Oops! 
            Think harder. You have another chance.
            But this will be the last.
                        """)
                    else:
                        self.slow.slow_print(Fore.RED + """
            You have lost the final chance. 
            You were unable to solve the riddle. 

    =====================GAME OVER=======================
                        """)

                        self.leader_board.leader_board(username, player_points, player_health, game_status)
                        raise SystemExit
                else:
                    self.slow.slow_print(Fore.GREEN + """
            Please choose from above options only.
                        """)
        except SystemExit:
            # If SystemExit is raised, catch it here
            pass
