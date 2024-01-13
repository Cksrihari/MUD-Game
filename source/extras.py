import time
import sys
from colorama import init
from colorama import Fore
init()

class Extras:
    def slow_print(self, text):  # Delayed printing function
        for character in text:
            sys.stdout.write(character)  # writes the character
            sys.stdout.flush()
            time.sleep(0.002)

    def help(self):
        self.slow_print(Fore.GREEN + """
            Commands to help you:
            i - display inventory
            enter - enter into a chamber
            open - open a chest
            unlock - unlock a chest or a door
            attack - attack an enemy
            take - take an item
                red - to pick red key
                green - to pick green key
            smash - smash pot
            heal - use health potion
            exit - exit game
            """)

    @staticmethod
    def inventory(armor, sharp_sword, health_potion, green_key, red_key):
        inventory_dict = {
            "Rusty Sword": True,
            "Armor": armor,
            "Sharp Sword": sharp_sword,
            "Health Potion": health_potion,
            "Green Key": green_key,
            "Red Key": red_key
        }
        for item in inventory_dict:
            if inventory_dict[item]:
                print(Fore.GREEN + """
                """ + item)


