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
                print("""
                """ + item)


