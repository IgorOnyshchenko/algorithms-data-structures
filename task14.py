import unittest
from io import StringIO
from unittest.mock import patch


def task14():
    n = int(input())
    commands = [input() for _ in range(n)]

    # assuming first command is 'push n'
    stack, maxs, num = [], [], int(commands[0].split()[1])
    stack.append(num)
    maxs.append(num)

    for cmd in commands[1:]:
        if cmd.startswith('push'):
            num = int(cmd.split()[1])
            stack.append(num)
            maxs.append(max(maxs[-1], num))
        elif cmd == 'pop':
            stack.pop()
            maxs.pop()
        elif cmd == 'max':
            print(maxs[-1])


class Task14TestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test1(self, mock_stdout):
        user_input = ['5', 'push 2', 'push 1', 'max', 'pop', 'max']
        with patch('builtins.input', side_effect=user_input):
            task14()
            self.assertEqual(mock_stdout.getvalue(), '2\n2\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test2(self, mock_stdout):
        user_input = ['5', 'push 1', 'push 2', 'max', 'pop', 'max']
        with patch('builtins.input', side_effect=user_input):
            task14()
            self.assertEqual(mock_stdout.getvalue(), '2\n1\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test3(self, mock_stdout):
        user_input = ['10', 'push 2', 'push 3', 'push 9', 'push 7', 'push 2', 'max', 'max', 'max', 'pop', 'max']
        with patch('builtins.input', side_effect=user_input):
            task14()
            self.assertEqual(mock_stdout.getvalue(), '9\n9\n9\n9\n')


if __name__ == '__main__':
    unittest.main()