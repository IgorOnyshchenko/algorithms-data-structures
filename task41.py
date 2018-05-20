import unittest
from io import StringIO
from unittest.mock import patch


def task41():
    def pre_order(v):
        if v == -1:
            return
        v = tree[v]
        print(v[0], end=' ')
        pre_order(v[1])
        pre_order(v[2])

    def in_order(v):
        if v == -1:
            return
        v = tree[v]
        in_order(v[1])
        print(v[0], end=' ')
        in_order(v[2])

    def post_order(v):
        if v == -1:
            return
        v = tree[v]
        post_order(v[1])
        post_order(v[2])
        print(v[0], end=' ')

    n = int(input())
    tree = [list(map(int, input().split())) for _ in range(n)]
    in_order(0)
    print()
    pre_order(0)
    print()
    post_order(0)


class Task41TestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test1(self, mock_stdout):
        user_input = ['5', '4 1 2', '2 3 4', '5 -1 -1', '1 -1 -1', '3 -1 -1']
        with patch('builtins.input', side_effect=user_input):
            task41()
            self.assertEqual(mock_stdout.getvalue(), '1 2 3 4 5 \n4 2 1 3 5 \n1 3 2 5 4 ')

    @patch('sys.stdout', new_callable=StringIO)
    def test2(self, mock_stdout):
        user_input = ['10', '0 7 2', '10 -1 -1', '20 -1 6', '30 8 9', '40 3 -1', '50 -1 -1', '60 1 -1', '70 5 4', '80 -1 -1', '90 -1 -1']
        with patch('builtins.input', side_effect=user_input):
            task41()
            self.assertEqual(mock_stdout.getvalue(), '50 70 80 30 90 40 0 20 10 60 \n0 70 50 40 30 80 90 20 60 10 \n50 80 90 30 40 70 10 60 20 0 ')


if __name__ == '__main__':
    unittest.main()