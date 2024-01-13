import unittest
from unittest.mock import patch, mock_open
from registration import PlayerRegistration  # Replace with your actual module name


class TestWelcomePage(unittest.TestCase):
    @patch('builtins.input', side_effect=['3'])
    def test_welcome_page_quit(self, mock_input):
        registration = PlayerRegistration()
        with self.assertRaises(SystemExit):
            registration.welcome_page()
        # Additional checks for the '1' and '2' choices can be added here


class TestRegisterAndCharCreate(unittest.TestCase):
    @patch('builtins.input', side_effect=['new_user', 'M', '1'])
    @patch('stdiomask.getpass', side_effect=['password'])
    @patch('builtins.open', new_callable=mock_open, read_data='')
    def test_register_and_char_create(self, mock_file, mock_getpass, mock_input):
        registration = PlayerRegistration()
        registration.register_and_char_create()
        # Assertions and checks for the registration process
        # Include tests for username and password validations


class TestLogin(unittest.TestCase):
    @patch('builtins.input', return_value='user1')
    @patch('stdiomask.getpass', return_value='password')
    @patch('builtins.open', new_callable=mock_open, read_data='user1:password\n')
    def test_login_success(self, mock_file, mock_getpass, mock_input):
        registration = PlayerRegistration()
        user_name = registration.login()
        self.assertEqual(user_name, 'user1')
        # Add more checks for unsuccessful login attempts





