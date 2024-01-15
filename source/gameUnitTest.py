import unittest
from unittest.mock import patch, mock_open
from game import GamePlay
from registration import PlayerRegistration
from HTMLTestRunner import HTMLTestRunner
from datetime import datetime, timezone
import calendar
import time
import random
import string


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = GamePlay()
        self.register = PlayerRegistration()


class TestLogin(TestGame):
    @patch('builtins.input', return_value='aa')
    @patch('stdiomask.getpass', return_value='11111')
    def test_user_name(self, mock_input, mock_getpass):
        self.register.login()
        self.assertGreater(len(self.register.user_name), 0, "Username should be greater than 0 characters")


class TestPlayerRegistration(TestGame):

    @patch('builtins.input', side_effect=['new_user', 'M', '1'])
    @patch('stdiomask.getpass', return_value='valid_pass')
    @patch('builtins.open', new_callable=mock_open, read_data='')
    def test_valid_registration(self, mock_file, mock_getpass, mock_input):
        self.register.register_and_char_create()
        # Assertions
        self.assertEqual(self.register.user_name, 'new_user', "Username should be 'new_user'")
        self.assertEqual(self.register.password, 'valid_pass', "Password should be 'valid_pass'")
        self.assertIn(self.register.selected_character, ['Nord', 'Elf', 'Orc', 'Dwarf'],
                      "Character should be one of the specified types")

    def generate_random_username(self, length=8):
        """Generate a random username."""
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @patch('builtins.input')
    @patch('stdiomask.getpass', return_value='test_password')
    def test_username_cannot_be_blank(self, mock_getpass, mock_input):
        random_username = self.generate_random_username()
        mock_input.side_effect = ['', random_username, 'M', '1']
        self.register.register_and_char_create()
        # Assertions
        self.assertNotEqual(self.register.user_name, '', "Username should not be blank")
        self.assertEqual(self.register.user_name, random_username, "Username should be randomly generated")
        self.assertEqual(self.register.char_sex, 'M')
        self.assertEqual(self.register.selected_character, 'Nord')
        self.assertEqual(self.register.password, 'test_password')


class TestSmash(TestGame):
    def test_pot_smash_points(self):
        self.game.pot_smash(1)
        self.assertEqual(self.game.player_points, 10)
        self.assertNotEqual(self.game.player_points, 0)

    def test_multiple_smash_points(self):
        for _ in range(5):
            self.game.pot_smash(1)
        self.assertEqual(self.game.player_points, 50)
        self.assertNotEqual(self.game.player_points, 0)


class TestAttack(TestGame):
    def test_attack(self):
        self.game.attack()
        self.assertEqual(self.game.player_health, 4)
        self.assertEqual(self.game.player_points, 10)
        self.assertNotEqual(self.game.player_health, 5)
        self.assertNotEqual(self.game.player_health, 0)

    def test_multiple_attack(self):
        for _ in range(4):
            self.game.attack()
        self.assertEqual(self.game.player_health, 1)
        self.assertEqual(self.game.player_points, 40)
        self.assertNotEqual(self.game.player_health, 5)
        self.assertNotEqual(self.game.player_health, 0)

class TestSlayed(TestGame):
    def test_slayed_with_full_health(self):
        for _ in range(5):
            self.game.attack()
            self.game.slayed()
        self.assertEqual(self.game.player_health, 0)
        self.assertNotEqual(self.game.player_health, 5)


class TestHeal(TestGame):
    def test_heal_when_health_full_and_no_health_potion(self):
        self.game.heal()
        self.assertEqual(self.game.player_health, 5)

    def test_heal_when_health_not_full_and_no_health_potion(self):
        self.game.attack()
        self.game.heal()
        self.assertEqual(self.game.player_health, 4)
        self.assertNotEqual(self.game.player_health, 5)

    def test_heal_when_health_not_full_and_has_health_potion(self):
        self.game.attack()
        self.game.has_health_potion = True
        self.game.heal()
        self.assertEqual(self.game.player_health, 5)
        self.assertNotEqual(self.game.player_health, 4)


if __name__ == "__main__":
    current_GMT = time.gmtime()
    time_stamp = calendar.timegm(current_GMT)
    current_time = datetime.fromtimestamp(time_stamp, timezone.utc).strftime("%Y-%m-%d %H_%M_%S")
    report_filename = f"../Reports/report_{current_time}.html"

    with open(report_filename, "w") as report_file:
        runner = HTMLTestRunner(
            stream=report_file,
            title='MUD-Game Unit Test Report',
            description='This demonstrates the detailed report of the unit test'
        )
        unittest.main(testRunner=runner)


