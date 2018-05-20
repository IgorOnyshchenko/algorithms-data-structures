import unittest
from io import StringIO
from unittest.mock import patch


def task11():
    seq = list(input())
    stack = []
    corresponding = {'}': '{', ')': '(', ']': '['}

    for (index, char) in enumerate(seq, start=1):
        if char in ['[', '{', '(']:
            stack.append((char, index))
        elif char in [']', '}', ')']:
            if len(stack) != 0 and (stack[-1][0] == corresponding[char]):
                stack.pop()
            else:
                print(index)
                return

    if len(stack) == 0:
        print('Success')
    else:
        print(stack[-1][1])


class Task11TestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test1(self, mock_stdout):
        user_input = ['[]']
        with patch('builtins.input', side_effect=user_input):
            task11()
            self.assertEqual(mock_stdout.getvalue(), 'Success\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test2(self, mock_stdout):
        user_input = ['{}[]']
        with patch('builtins.input', side_effect=user_input):
            task11()
            self.assertEqual(mock_stdout.getvalue(), 'Success\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test3(self, mock_stdout):
        user_input = ['[()]']
        with patch('builtins.input', side_effect=user_input):
            task11()
            self.assertEqual(mock_stdout.getvalue(), 'Success\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test4(self, mock_stdout):
        user_input = ['(())']
        with patch('builtins.input', side_effect=user_input):
            task11()
            self.assertEqual(mock_stdout.getvalue(), 'Success\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test5(self, mock_stdout):
        user_input = ['{[]}()']
        with patch('builtins.input', side_effect=user_input):
            task11()
            self.assertEqual(mock_stdout.getvalue(), 'Success\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test6(self, mock_stdout):
        user_input = ['{']
        with patch('builtins.input', side_effect=user_input):
            task11()
            self.assertEqual(mock_stdout.getvalue(), '1\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test7(self, mock_stdout):
        user_input = ['{[}']
        with patch('builtins.input', side_effect=user_input):
            task11()
            self.assertEqual(mock_stdout.getvalue(), '3\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test8(self, mock_stdout):
        user_input = ['foo(bar);']
        with patch('builtins.input', side_effect=user_input):
            task11()
            self.assertEqual(mock_stdout.getvalue(), 'Success\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test9(self, mock_stdout):
        user_input = ['foo(bar[i);']
        with patch('builtins.input', side_effect=user_input):
            task11()
            self.assertEqual(mock_stdout.getvalue(), '10\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test10(self, mock_stdout):
        user_input = ['([](){([])})']
        with patch('builtins.input', side_effect=user_input):
            task11()
            self.assertEqual(mock_stdout.getvalue(), 'Success\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test11(self, mock_stdout):
        user_input = ['()[]}']
        with patch('builtins.input', side_effect=user_input):
            task11()
            self.assertEqual(mock_stdout.getvalue(), '5\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test12(self, mock_stdout):
        user_input = ['{{[()]]']
        with patch('builtins.input', side_effect=user_input):
            task11()
            self.assertEqual(mock_stdout.getvalue(), '7\n')

if __name__ == '__main__':
    unittest.main()