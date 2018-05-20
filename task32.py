import unittest
from io import StringIO
from unittest.mock import patch


def polyhash(word, m, x=263, p=1000000007):
    hash = 0
    for c in reversed(word):
        hash = (hash * x + ord(c)) % p
    return hash % m


def task32():
    m = int(input())
    book = {}
    for _ in range(int(input())):
        command = input().split()
        if command[0] == 'add':
            hash = polyhash(command[1], m)
            bin = book.get(hash, None)
            if bin:
                if command[1] not in bin:
                    book[hash] = [command[1]] + bin
            else:
                book[hash] = [command[1]]
        elif command[0] == 'find':
            hash = polyhash(command[1], m)
            bin = book.get(hash, [])
            print('yes' if command[1] in bin else 'no')
        elif command[0] == 'check':
            bin = book.get(int(command[1]), [])
            print(*bin)
        else:
            hash = polyhash(command[1], m)
            bin = book.get(hash, [])
            if command[1] in bin:
                bin.remove(command[1])


class Task32TestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test1(self, mock_stdout):
        user_input = ['5', '12', 'add world', 'add HellO', 'check 4', 'find World', 'find world', 'del world', 'check 4', 'del HellO', 'add luck', 'add GooD', 'check 2', 'del good']
        with patch('builtins.input', side_effect=user_input):
            task32()
            self.assertEqual(mock_stdout.getvalue(), 'HellO world\nno\nyes\nHellO\nGooD luck\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test2(self, mock_stdout):
        user_input = ['4', '8', 'add test', 'add test', 'find test', 'del test', 'find test', 'find Test', 'add Test', 'find Test']
        with patch('builtins.input', side_effect=user_input):
            task32()
            self.assertEqual(mock_stdout.getvalue(), 'yes\nno\nno\nyes\n')


if __name__ == '__main__':
    unittest.main()