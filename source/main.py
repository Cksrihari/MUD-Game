from functionsMUDGame import functions_MUD

class Main(object):
    def __init__(self):
        self.mud_game = functions_MUD()

    def main(self):
        while True:
            self.mud_game.img()
            self.mud_game.welcomePage()


if __name__ == "__main__":
    main = Main()
    main.main()
