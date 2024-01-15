import time
import sys
from colorama import init
from colorama import Fore
import pygame
init()


class Extras:
    @staticmethod
    def slow_print(text):  # Delayed printing function
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
            c - Show character details
            exit - exit game
                        """)

    def inventory(self, armor, adv_weapon, health_potion, green_key, red_key):
        inventory_dict = {
            "Rusty Sword": True,
            "Armor": armor,
            "Advanced Weapon": adv_weapon,
            "Health Potion": health_potion,
            "Green Key": green_key,
            "Red Key": red_key
        }
        for item in inventory_dict:
            if inventory_dict[item]:
                self.slow_print(Fore.GREEN + """
            """ + item + """
                        """)

    @staticmethod
    def play_game_audio():
        soundtrack_path = "../resources/game_audio.mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(soundtrack_path)
        pygame.mixer.music.play(-1)  # -1 for looping the music
