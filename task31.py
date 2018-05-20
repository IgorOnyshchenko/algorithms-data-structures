import unittest
from io import StringIO
from unittest.mock import patch


def task31():
    book = {}
    for _ in range(int(input())):
        command = input().split()
        if command[0] == 'add':
            book[command[1]] = command[2]
        elif command[0] == 'find':
            print(book.get(command[1], 'not found'))
        else:
            book.pop(command[1], None)


class Task31TestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test1(self, mock_stdout):
        user_input = ['12', 'add 911 police', 'add 76213 Mom', 'add 17239 Bob', 'find 76213', 'find 910', 'find 911', 'del 910', 'del 911', 'find 911', 'find 76213', 'add 76213 daddy', 'find 76213']
        with patch('builtins.input', side_effect=user_input):
            task31()
            self.assertEqual(mock_stdout.getvalue(), 'Mom\nnot found\npolice\nnot found\nMom\ndaddy\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test2(self, mock_stdout):
        user_input = ['8', 'find 3839442', 'add 123456 me', 'add 0 granny', 'find 0', 'find 123456', 'del 0', 'del 0', 'find 0']
        with patch('builtins.input', side_effect=user_input):
            task31()
            self.assertEqual(mock_stdout.getvalue(), 'not found\ngranny\nme\nnot found\n')


if __name__ == '__main__':
    unittest.main()