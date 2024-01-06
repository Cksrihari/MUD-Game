from registration import playerRegistration
from intro import introduction
from game import GamePlay
class Main(object):
    def __init__(self):
        self.register = playerRegistration()
        self.intro = introduction()
        self.game = GamePlay()


    def main(self):
        self.intro.img()
        self.intro.introScenario()
        self.register.welcomePage()
        self.game.starting_prompt()
        self.game.common_chamber()

if __name__ == "__main__":
    main = Main()
    main.main()
