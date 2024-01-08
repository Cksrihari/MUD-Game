from registration import PlayerRegistration
from intro import Introduction
from game import GamePlay


class Main(object):
    def __init__(self):
        self.register = PlayerRegistration()
        self.intro = Introduction()
        self.game = GamePlay()

    def main(self):
        self.intro.img()
        self.intro.introScenario()
        self.register.welcomePage()
        self.game.gamePlay()
        self.game.starting_prompt()



if __name__ == "__main__":
    main = Main()
    main.main()
