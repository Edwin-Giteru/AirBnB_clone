import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def test_quit(self):
        self.assertTrue(self.console.do_quit(""))

    def test_EOF(self):
        self.assertTrue(self.console.do_EOF(""))

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_missing_class(self, mock_stdout):
        self.console.do_create("")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class name is missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_invalid_class(self, mock_stdout):
        self.console.do_create("InvalidClass")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_missing_class(self, mock_stdout):
        self.console.do_show("")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class name is missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_missing_id(self, mock_stdout):
        self.console.do_show("BaseModel")
        self.assertEqual(mock_stdout.getvalue().strip(), "** instance id is missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_missing_class(self, mock_stdout):
        self.console.do_destroy("")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class name is missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_invalid_class(self, mock_stdout):
        self.console.do_all("InvalidClass")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_missing_class(self, mock_stdout):
        self.console.do_update("")
        self.assertEqual(mock_stdout.getvalue().strip(), "** class name missing **")

if __name__ == '__main__':
    unittest.main()
