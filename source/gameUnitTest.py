import unittest
import datetime
from unittest.mock import patch, mock_open
from game import GamePlay
from registration import PlayerRegistration

from HTMLTestRunner import HTMLTestRunner



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


class TestRegister(TestGame):
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

    class TestPlayerRegistration(TestGame):
        @patch('builtins.input', side_effect=['', 'valid_user'])
        @patch('stdiomask.getpass', return_value='valid_pass')
        @patch('builtins.open', new_callable=mock_open, read_data='')
        def test_username_cannot_be_blank(self, mock_file, mock_getpass, mock_input):
            self.register.register_and_char_create()
            # Assertions
            self.assertNotEqual(self.register.user_name, '', "Username should not be blank")
            self.assertEqual(self.register.user_name, 'valid_user', "Username should be 'valid_user'")


class TestSmash(TestGame):
    def test_pot_smash_points(self):
        self.game.pot_smash(1)
        self.assertEqual(self.game.player_points, 10)

    def test_multiple_smash_points(self):
        for _ in range(5):
            self.game.pot_smash(1)
        self.assertEqual(self.game.player_points, 50)


class TestAttack(TestGame):
    def test_attack(self):
        self.game.attack()
        self.assertEqual(self.game.player_health, 4)
        self.assertEqual(self.game.player_points, 10)

    def test_multiple_attack(self):
        for _ in range(4):
            self.game.attack()
        self.assertEqual(self.game.player_health, 1)
        self.assertEqual(self.game.player_points, 40)


if __name__ == '__main__':
    # Generating file name based on current date and time
    current_time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    report_filename = f"../TestReport/report_{current_time}.html"

    unittest.main(testRunner=HTMLTestRunner(output=report_filename))
