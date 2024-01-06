from extras import Extras


class Introduction:

    def __init__(self):
        self.slow = Extras()

    def img(self):

        self.slow.slowPrint("""

                ░██████╗██╗░░░██╗██████╗░███████╗██████╗    ██╗░░██╗███╗░░██╗██╗░██████╗░██╗░░██╗████████╗
                ██╔════╝██║░░░██║██╔══██╗██╔════╝██╔══██╗   ██║░██╔╝████╗░██║██║██╔════╝░██║░░██║╚══██╔══╝
                ╚█████╗░██║░░░██║██████╔╝█████╗░░██████╔╝   █████═╝░██╔██╗██║██║██║░░██╗░███████║░░░██║░░░
                ░╚═══██╗██║░░░██║██╔═══╝░██╔══╝░░██╔══██╗   ██╔═██╗░██║╚████║██║██║░░╚██╗██╔══██║░░░██║░░░
                ██████╔╝╚██████╔╝██║░░░░░███████╗██║░░██║   ██║░╚██╗██║░╚███║██║╚██████╔╝██║░░██║░░░██║░░░
                ╚═════╝░░╚═════╝░╚═╝░░░░░╚══════╝╚═╝░░╚═╝   ╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░
                """)

    def introScenario(self):
        self.slow.slowPrint("""
                    Join the adventure in 'Super Knight' as a brave knight who loves a princess! 
                                              Explore a castle, 
                                         fight guards, solve quests 
                                                    AND 
                        Save the princess from a king who doesn't want them to be together.
                        """)
