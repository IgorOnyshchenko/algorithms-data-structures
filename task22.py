import unittest
import heapq
from io import StringIO
from unittest.mock import patch


def task22():
    nproc, _ = list(map(int, input().split()))
    task_times = list(map(int, input().split()))
    heap = [[0, i] for i in range(nproc)]
    for task_time in task_times:
        item = heapq.heappop(heap)
        print(item[1], item[0])
        item[0] += task_time
        heapq.heappush(heap, item)


class Task22TestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test1(self, mock_stdout):
        user_input = ['2 5', '1 2 3 4 5']
        with patch('builtins.input', side_effect=user_input):
            task22()
            self.assertEqual(mock_stdout.getvalue(), '0 0\n1 0\n0 1\n1 2\n0 4\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test2(self, mock_stdout):
        user_input = ['4 20', '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1']
        with patch('builtins.input', side_effect=user_input):
            task22()
            self.assertEqual(mock_stdout.getvalue(), '0 0\n1 0\n2 0\n3 0\n0 1\n1 1\n2 1\n3 1\n0 2\n1 2\n2 2\n3 2\n0 3\n1 3\n2 3\n3 3\n0 4\n1 4\n2 4\n3 4\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test3(self, mock_stdout):
        user_input = ['2 15', '0 0 1 0 0 0 2 1 2 3 0 0 0 2 1']
        with patch('builtins.input', side_effect=user_input):
            task22()
            self.assertEqual(mock_stdout.getvalue(), '0 0\n0 0\n0 0\n1 0\n1 0\n1 0\n1 0\n0 1\n0 2\n1 2\n0 4\n0 4\n0 4\n0 4\n1 5\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test4(self, mock_stdout):
        user_input = ['4 10', '3 0 9 2 8 1 9 8 8 4']
        with patch('builtins.input', side_effect=user_input):
            task22()
            self.assertEqual(mock_stdout.getvalue(), '0 0\n1 0\n1 0\n2 0\n3 0\n2 2\n0 3\n2 3\n3 8\n1 9\n')


if __name__ == '__main__':
    unittest.main()