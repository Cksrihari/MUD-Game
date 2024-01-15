import unittest

from unittest.mock import patch
from game import GamePlay
from registration import PlayerRegistration
from HTMLTestRunner import HTMLTestRunner
from datetime import datetime, timezone
import calendar
import time
from tasks import Task
from io import StringIO
import sys
from leaderBoard import LeaderBoard


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = GamePlay()
        self.register = PlayerRegistration()
        self.task = Task()
        self.register = PlayerRegistration()
        self.task = Task()
        self.leader_board = LeaderBoard


class TestLogin(TestGame):
    @patch('builtins.input', return_value='aa')
    @patch('stdiomask.getpass', return_value='11111')
    def test_user_name(self, mock_input, mock_getpass):
        self.register.login()
        self.assertGreater(len(self.register.user_name), 0, "Username should be greater than 0 characters")


class TestRegisterAddUsername(TestGame):

    @patch('builtins.input', side_effect=['', '', 'valid_username'])
    def test_register_add_username_blank_input(self, mock_input):
        with self.assertRaises(SystemExit) as cm:
            self.register.register_add_username()

        self.assertEqual(cm.exception.code, 1, "SystemExit code should be 1 for blank input")

    @patch('builtins.input', side_effect=['valid_username'])
    def test_register_add_username_valid_input(self, mock_input):
        self.register = PlayerRegistration()

        self.register.register_add_username()

        # Assuming you have an attribute to store the entered username, you can assert it
        self.assertEqual(self.register.user_name, 'valid_username', "Username should be set to 'valid_username'")


class TestRegisterAddPass(TestGame):
    @patch('stdiomask.getpass', return_value='valid_password')
    def test_register_add_pass_valid_input(self, mock_getpass):
        with patch('builtins.input', side_effect=['valid_password']):
            captured_output = StringIO()
            sys.stdout = captured_output

            self.register.register_add_pass()

            sys.stdout = sys.__stdout__  # Reset redirection
            printed_output = captured_output.getvalue()

            # Assertions
            self.assertIn("Registration successful!\nCreate your character.", printed_output)

class TestGender(TestGame):
    @patch('builtins.input', return_value='M')
    def test_register_add_gender_valid_input(self, mock_input):
        self.register.register_add_gender()
        self.assertEqual(self.register.char_sex, 'M')

    @patch('builtins.input', return_value='F')  # Mocking user input for testing
    def test_register_add_gender_valid_input_female(self, mock_input):
        self.register.register_add_gender()
        self.assertEqual(self.register.char_sex, 'F')

    @patch('builtins.input', side_effect=['invalid', 'M'])  # Mocking user input for testing
    def test_register_add_gender_invalid_then_valid_input(self, mock_input):
        self.register.register_add_gender()
        self.assertEqual(self.register.char_sex, 'M')


class TestRegisterSelectCharacter(TestGame):
    @patch("builtins.input", side_effect=["2"])
    def test_register_select_character_valid_input(self, mock_input):
        self.register.register_select_character()

        # Assert
        self.assertEqual(self.register.selected_character, "Elf")

    @patch("builtins.input", side_effect=["5", "3"])
    def test_register_select_character_invalid_then_valid_input(self, mock_input):
        self.register.register_select_character()
        self.assertEqual(self.register.selected_character, "Orc")

    @patch("builtins.input", side_effect=["invalid", "4"])
    def test_register_select_character_invalid_then_valid_input_with_invalid_input(self, mock_input):
        self.register.register_select_character()
        self.assertEqual(self.register.selected_character, "Dwarf")

        
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


class TestTask(TestGame):
    @patch('builtins.input', return_value='A')
    def test_task_1_correct_answer(self, mock_input):

        captured_output = StringIO()
        sys.stdout = captured_output
        with self.assertRaises(SystemExit) as cm:
            self.task.task_1("TestUser", "Nord", 0, 100, "InProgress")
        self.assertIsInstance(cm.exception, SystemExit, "Expected a SystemExit exception to be raised")
        printed_output = captured_output.getvalue()
        expected_output = "Genius! As you are a Nord, you have been awarded the,"
        self.assertIn(expected_output, printed_output, f"Expected output: {expected_output}, Actual output: {printed_output}")

    @patch('builtins.input', side_effect=['A'])
    def test_task_2_correct_answer(self, mock_input):
        self.task = Task()
        captured_output = StringIO()
        sys.stdout = captured_output
        try:
            self.task.task_2("TestUser", 0, 100, "InProgress")
        except SystemExit as se:
            print(f"Caught SystemExit: {se}")
            self.assertEqual(se.code, 0, "Expected exit code to be 0")
        printed_output = captured_output.getvalue()
        expected_output = "Genius! You have been awarded a health potion, use it wisely."
        self.assertIn(expected_output, printed_output,
                      f"Expected output: {expected_output}, Actual output: {printed_output}")


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