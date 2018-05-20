import unittest
from io import StringIO
from unittest.mock import patch


def task24():
    def find(i):
        to_change_parent = []
        while i != parent[i]:
            to_change_parent.append(i)
            i = parent[i]
        for item in to_change_parent:
            parent[item] = i
        return i

    def union(dest, src):
        dest, src = find(dest), find(src)
        if dest != src:
            parent[src] = dest

    n, e, d = list(map(int, input().split()))
    parent = list(range(n+1))
    for _ in range(e):
        x1, x2 = list(map(int, input().split()))
        union(x1, x2)
    for _ in range(d):
        x1, x2 = list(map(int, input().split()))
        if find(x1) == find(x2):
            print(0)
            return
    print(1)


class Task24TestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test1(self, mock_stdout):
        user_input = ['4 6 0', '1 2', '1 3', '1 4', '2 3', '2 4', '3 4']
        with patch('builtins.input', side_effect=user_input):
            task24()
            self.assertEqual(mock_stdout.getvalue(), '1\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test2(self, mock_stdout):
        user_input = ['6 5 3', '2 3', '1 5', '2 5', '3 4', '4 2', '6 1', '4 6', '4 5']
        with patch('builtins.input', side_effect=user_input):
            task24()
            self.assertEqual(mock_stdout.getvalue(), '0\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test3(self, mock_stdout):
        user_input = ['4 6 1', '1 2', '1 3', '1 4', '2 3', '2 4', '3 4', '1 2']
        with patch('builtins.input', side_effect=user_input):
            task24()
            self.assertEqual(mock_stdout.getvalue(), '0\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test4(self, mock_stdout):
        user_input = ['4 0 6', '1 2', '1 3', '1 4', '2 3', '2 4', '3 4']
        with patch('builtins.input', side_effect=user_input):
            task24()
            self.assertEqual(mock_stdout.getvalue(), '1\n')


if __name__ == '__main__':
    unittest.main()