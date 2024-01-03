from registration import playerRegistration
from intro import introduction
from extras import extras
class Main(object):
    def __init__(self):
        self.register = playerRegistration()
        self.intro = introduction()

    def main(self):
        self.intro.img()
        self.intro.introScenario()
        self.register.welcomePage()



if __name__ == "__main__":
    main = Main()
    main.main()
