import unittest
from io import StringIO
from unittest.mock import patch


def task23():
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
            tables[dest] += tables[src]
        return tables[dest]

    n, m = list(map(int, input().split()))
    tables = [0] + list(map(int, input().split()))
    parent = list(range(n+1))
    result = max(tables)
    for _ in range(m):
        dest, src = list(map(int, input().split()))
        result = max(result, union(dest, src))
        print(result)


class Task23TestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test1(self, mock_stdout):
        user_input = ['5 5', '1 1 1 1 1', '3 5', '2 4', '1 4', '5 4', '5 3']
        with patch('builtins.input', side_effect=user_input):
            task23()
            self.assertEqual(mock_stdout.getvalue(), '2\n2\n3\n5\n5\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test2(self, mock_stdout):
        user_input = ['6 4', '10 0 5 0 3 3', '6 6', '6 5', '5 4', '4 3']
        with patch('builtins.input', side_effect=user_input):
            task23()
            self.assertEqual(mock_stdout.getvalue(), '10\n10\n10\n11\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test3(self, mock_stdout):
        user_input = ['6 4', '2 11 5 0 7 3', '6 6', '6 5', '5 4', '4 3']
        with patch('builtins.input', side_effect=user_input):
            task23()
            self.assertEqual(mock_stdout.getvalue(), '11\n11\n11\n15\n')


if __name__ == '__main__':
    unittest.main()