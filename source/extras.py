import time
import sys
class extras:
    def slowPrint(self, text):  # Delayed printing function
        for character in text:
            sys.stdout.write(character)  # writes the character
            sys.stdout.flush()
            time.sleep(0.02)  # this is the delay time between each character

