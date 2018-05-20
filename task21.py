import unittest
from io import StringIO
from unittest.mock import patch


def task21():
    def sift(i):
        imin, ileft, iright = i, 2 * i, 2 * i + 1
        if ileft <= size and heap[ileft] < heap[imin]:
            imin = ileft
        if iright <= size and heap[iright] < heap[imin]:
            imin = iright
        if i != imin:
            heap[i], heap[imin] = heap[imin], heap[i]
            swaps.append((i - 1, imin - 1))
            sift(imin)

    size = int(input())
    heap = [0] + list(map(int, input().split()))

    swaps = []
    for i in range(size // 2, 0, -1):
        sift(i)

    print(len(swaps))
    for swap in swaps:
        print(*swap)


class Task21TestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test1(self, mock_stdout):
        user_input = ['5', '5 4 3 2 1']
        with patch('builtins.input', side_effect=user_input):
            task21()
            self.assertEqual(mock_stdout.getvalue(), '3\n1 4\n0 1\n1 3\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test2(self, mock_stdout):
        user_input = ['5', '1 2 3 4 5']
        with patch('builtins.input', side_effect=user_input):
            task21()
            self.assertEqual(mock_stdout.getvalue(), '0\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test3(self, mock_stdout):
        user_input = ['6', '0 1 2 3 4 5']
        with patch('builtins.input', side_effect=user_input):
            task21()
            self.assertEqual(mock_stdout.getvalue(), '0\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test4(self, mock_stdout):
        user_input = ['6', '7 6 5 4 3 2']
        with patch('builtins.input', side_effect=user_input):
            task21()
            self.assertEqual(mock_stdout.getvalue(), '4\n2 5\n1 4\n0 2\n2 5\n')


if __name__ == '__main__':
    unittest.main()