from extras import Extras
from leaderBoard import LeaderBoard

class Task:
    def __init__(self):
        self.slow = Extras()
        self.leader_board = LeaderBoard()
    def task_1(self, username, player_points, player_health, game_status):
        self.slow.slowPrint("""
        You are now in the Main Chamber. The door is locked!
        You have to complete two riddled to open the door and move forward.
        Here comes the first riddle!

        Riddle: I have a face but no eyes, hands but no arms,
                A tick-tock sound, yet do no harm.
                What am I?
                    """)

        chance = 2
        while True:
            self.slow.slowPrint(f"""
        Chances Left: {chance}
                    """)
            answer_task_1 = input("""
        Options:
                a) Clock
                b) Statue
                c) Painting
                d) Mirror
        Answer: 
            """)

            if answer_task_1.upper() == "A":
                self.slow.slowPrint("""
        Genius! You have been awarded the Sharp sword. It'll help you to beat the Boss.
                    """)
                break
            elif answer_task_1.upper() in ["B", "C", "D"]:
                chance -= 1
                if chance > 0:
                    self.slow.slowPrint("""
        Oops! 
        Think harder. You have another chance.
        But this will be the last.
                    """)
                elif chance == 0:
                    self.slow.slowPrint("""
        You have lost the final chance. 
        You were unable to solve the riddle. 

=====================GAME OVER=======================
                    """)
                    self.leader_board.leaderBoard(username, player_points, player_health, game_status)
                    exit()
            else:
                self.slow.slowPrint("""
        Un-expected input. Please choose from above options only""")

    def task_2(self, username, player_points, player_health, game_status):
        self.slow.slowPrint("""
        Continue thinking hard. 
        This is the last one!

        Riddle: I'm shiny and bright, but not made of gold,
                I turn and twist, yet in place I hold.
                What am I?        
                    """)

        chance = 2
        while True:
            self.slow.slowPrint(f"""
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
                self.slow.slowPrint("""
        Genius! You have been awarded a health potion, use it wisely.
        Now you can enter the Boss Chamber.
                    """)
                break
            elif answer_task_2.upper() in ["B", "C", "D"]:
                chance -= 1
                if chance > 0:
                    self.slow.slowPrint("""
        Oops! 
        Think harder. You have another chance.
        But this will be the last.
                    """)
                elif chance == 0:
                    self.slow.slowPrint("""
        You have lost the final chance. 
        You were unable to solve the riddle. 

=====================GAME OVER=======================
                    """)
                    self.leader_board.leaderBoard(username, player_points, player_health, game_status)
                    exit()
            else:
                self.slow.slowPrint("""
                Un-expected input. Please choose from above options only""")


if __name__ == "__main__":
    task = Task()
    task.task_1()
    task.task_2()
