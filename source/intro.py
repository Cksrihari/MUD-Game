from extras import Extras


class Introduction:

    def __init__(self):
        self.slow = Extras()

    def img(self):
        name = open("../resources/gameName.txt", "r")
        self.slow.slow_print(name)
        self.slow.slow_print("")

    def intro_scenario(self):
        self.slow.slow_print("""
                    Join the adventure in 'Super Knight' as a brave knight who loves a princess! 
                                              Explore a castle, 
                                         fight guards, solve quests 
                                                    AND 
                        Save the princess from a king who doesn't want them to be together.
                        """)
