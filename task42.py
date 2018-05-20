import unittest
import sys
from io import StringIO
from unittest.mock import patch


def task42():
    VALUE_MAX = 2**31
    VALUE_MIN = -VALUE_MAX

    def is_bst(node, mini, maxi):
        if node == -1:
            return True

        node = tree[node]
        if node[0] < mini or node[0] > maxi:
            return False

        return (is_bst(node[1], mini, node[0] - 1) and
                is_bst(node[2], node[0] + 1, maxi))

    n = int(input())
    sys.setrecursionlimit(20000)
    tree = [list(map(int, input().split())) for _ in range(n)]
    print('CORRECT' if is_bst(-1 if n == 0 else 0, VALUE_MIN, VALUE_MAX) else 'INCORRECT')


class Task42TestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test1(self, mock_stdout):
        user_input = ['3', '2 1 2', '1 -1 -1', '3 -1 -1']
        with patch('builtins.input', side_effect=user_input):
            task42()
            self.assertEqual(mock_stdout.getvalue(), 'CORRECT\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test2(self, mock_stdout):
        user_input = ['3', '1 1 2', '2 -1 -1', '3 -1 -1']
        with patch('builtins.input', side_effect=user_input):
            task42()
            self.assertEqual(mock_stdout.getvalue(), 'INCORRECT\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test3(self, mock_stdout):
        user_input = ['0']
        with patch('builtins.input', side_effect=user_input):
            task42()
            self.assertEqual(mock_stdout.getvalue(), 'CORRECT\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test4(self, mock_stdout):
        user_input = ['5', '1 -1 1', '2 -1 2', '3 -1 3', '4 -1 4', '5 -1 -1']
        with patch('builtins.input', side_effect=user_input):
            task42()
            self.assertEqual(mock_stdout.getvalue(), 'CORRECT\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test5(self, mock_stdout):
        user_input = ['7', '4 1 2', '2 3 4', '6 5 6', '1 -1 -1', '3 -1 -1', '5 -1 -1', '7 -1 -1']
        with patch('builtins.input', side_effect=user_input):
            task42()
            self.assertEqual(mock_stdout.getvalue(), 'CORRECT\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test6(self, mock_stdout):
        user_input = ['4', '4 1 -1', '2 2 3', '1 -1 -1', '5 -1 -1']
        with patch('builtins.input', side_effect=user_input):
            task42()
            self.assertEqual(mock_stdout.getvalue(), 'INCORRECT\n')


if __name__ == '__main__':
    unittest.main()