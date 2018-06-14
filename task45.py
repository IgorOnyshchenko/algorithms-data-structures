import unittest
from io import StringIO
from unittest.mock import patch


def task45():
    string = input()
    n = int(input())
    for _ in range(n):
        i, j, k = map(int, input().split())
        substring = string[i:j+1]
        string = string[:i] + string[j+1:]
        string = string[:k] + substring + string[k:]
    print(string)


class Task45TestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test1(self, mock_stdout):
        user_input = ['hlelowrold', '2', '1 1 2', '6 6 7']
        with patch('builtins.input', side_effect=user_input):
            task45()
            self.assertEqual(mock_stdout.getvalue(), 'helloworld\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test2(self, mock_stdout):
        user_input = ['abcdef', '2', '0 1 1', '4 5 0']
        with patch('builtins.input', side_effect=user_input):
            task45()
            self.assertEqual(mock_stdout.getvalue(), 'efcabd\n')


if __name__ == '__main__':
    unittest.main()