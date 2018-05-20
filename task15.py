import unittest
from io import StringIO
from unittest.mock import patch
from collections import deque


def task15():
    n = int(input())
    seq = list(map(int, input().split()))
    sz = int(input())

    if n is None:
        n = int(input())
    if seq is None:
        seq = map(int, input().split())
    if sz is None:
        sz = int(input())

    deq, maxs = deque(), []
    for i in range(n):
        if len(deq) != 0 and deq[0] < i - sz + 1:
            deq.popleft()
        while len(deq) != 0 and seq[deq[-1]] < seq[i]:
            deq.pop()
        deq.append(i)
        if i >= sz - 1:
            maxs.append(seq[deq[0]])

    print(*maxs)


class Task15TestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test1(self, mock_stdout):
        user_input = ['3', '2 1 5', '1']
        with patch('builtins.input', side_effect=user_input):
            task15()
            self.assertEqual(mock_stdout.getvalue(), '2 1 5\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test2(self, mock_stdout):
        user_input = ['3', '2 3 9', '3']
        with patch('builtins.input', side_effect=user_input):
            task15()
            self.assertEqual(mock_stdout.getvalue(), '9\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test3(self, mock_stdout):
        user_input = ['8', '2 7 3 1 5 2 6 2', '4']
        with patch('builtins.input', side_effect=user_input):
            task15()
            self.assertEqual(mock_stdout.getvalue(), '7 7 5 6 6\n')


if __name__ == '__main__':
    unittest.main()