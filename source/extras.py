import time
import sys

class Extras:

    def slowPrint(self, text):  # Delayed printing function
        for character in text:
            sys.stdout.write(character)  # writes the character
            sys.stdout.flush()
            time.sleep(0.002)

    def help(self):
        self.slowPrint("""
            Commands to help you:
            i - display inventory
            enter - enter into a chamber
            open - open a chest
            unlock - unlock a chest or a door
            attack - attack an enemy
            take - take an item
            heal - use health potion
            exit - exit game
            """)

