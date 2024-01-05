from extras import extras


class introduction:

    def __init__(self):
        self.slow = extras()

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
        self.slow.slowPrint("\nJoin the adventure in 'Super Knight' as a brave knight who loves a princess! \nExplore a castle, fight guards, solve quests \n\n\t\tAND \n\nSave the princess from a king who doesn't want them to be together.\n\n")
