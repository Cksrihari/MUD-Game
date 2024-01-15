from registration import PlayerRegistration
from intro import Introduction
from game import GamePlay
from leaderBoard import LeaderBoard
from extras import Extras


class Main(object):
    def __init__(self):
        self.register = PlayerRegistration()
        self.intro = Introduction()
        self.game = GamePlay()
        self.leaderBoard = LeaderBoard()
        self.music = Extras()

    def main(self):
        self.music.play_game_audio()
        self.intro.img()
        self.intro.intro_scenario()
        self.register.welcome_page()
        self.game.game_play()


if __name__ == "__main__":
    main = Main()
    main.main()
