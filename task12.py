import unittest
from io import StringIO
from unittest.mock import patch


def task12():
    def get_depth(idx):
        depth = depths.get(idx, None)
        if depth:
            return depth
        parent = parents[idx]
        if parent == -1:
            depth = 1
        else:
            depth = get_depth(parent) + 1
        depths[idx] = depth
        return depth

    int(input())
    parents = list(map(int, input().split()))
    depths = {}
    max_depth = 0

    for idx, parent in enumerate(parents):
        depth = get_depth(idx)
        if depth > max_depth:
            max_depth = depth

    print(max_depth)


class Task12TestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test1(self, mock_stdout):
        user_input = ['5', '4 -1 4 1 1']
        with patch('builtins.input', side_effect=user_input):
            task12()
            self.assertEqual(mock_stdout.getvalue(), '3\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test2(self, mock_stdout):
        user_input = ['5', '-1 0 4 0 3']
        with patch('builtins.input', side_effect=user_input):
            task12()
            self.assertEqual(mock_stdout.getvalue(), '4\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test3(self, mock_stdout):
        user_input = ['10', '9 7 5 5 2 9 9 9 2 -1']
        with patch('builtins.input', side_effect=user_input):
            task12()
            self.assertEqual(mock_stdout.getvalue(), '4\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test4(self, mock_stdout):
        user_input = ['1', '-1']
        with patch('builtins.input', side_effect=user_input):
            task12()
            self.assertEqual(mock_stdout.getvalue(), '1\n')


if __name__ == '__main__':
    unittest.main()