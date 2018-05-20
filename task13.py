import unittest
from io import StringIO
from collections import deque
from unittest.mock import patch


def task13():
    size, n = list(map(int, input().split()))
    packets = [[int(item) for item in input().split()] for _ in range(n)]

    buffer = deque()
    times, na_count = [], 0

    for packet in packets:
        t, d = packet
        while len(buffer) != 0 and buffer[-1][1] <= t:
            if buffer[-1][0] == -1:
                na_count -= 1
            times.append(buffer[-1][0])
            buffer.pop()
        if len(buffer)-na_count < size:
            if len(buffer) == 0:
                buffer.appendleft((t, t+d))
            else:
                buffer.appendleft((buffer[0][1], buffer[0][1]+d))
        else:
            buffer.appendleft((-1, buffer[0][1]))
            na_count += 1

    while len(buffer) != 0:
        times.append(buffer[-1][0])
        buffer.pop()

    print(*times, sep='\n')


class Task13TestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test1(self, mock_stdout):
        user_input = ['1 0']
        with patch('builtins.input', side_effect=user_input):
            task13()
            self.assertEqual(mock_stdout.getvalue(), '\n')


    @patch('sys.stdout', new_callable=StringIO)
    def test2(self, mock_stdout):
        user_input = ['1 1', '0 0']
        with patch('builtins.input', side_effect=user_input):
            task13()
            self.assertEqual(mock_stdout.getvalue(), '0\n')


    @patch('sys.stdout', new_callable=StringIO)
    def test3(self, mock_stdout):
        user_input = ['1 1', '0 1']
        with patch('builtins.input', side_effect=user_input):
            task13()
            self.assertEqual(mock_stdout.getvalue(), '0\n')


    @patch('sys.stdout', new_callable=StringIO)
    def test4(self, mock_stdout):
        user_input = ['1 2', '0 1', '0 1']
        with patch('builtins.input', side_effect=user_input):
            task13()
            self.assertEqual(mock_stdout.getvalue(), '0\n-1\n')


    @patch('sys.stdout', new_callable=StringIO)
    def test5(self, mock_stdout):
        user_input = ['1 2', '0 1', '1 1']
        with patch('builtins.input', side_effect=user_input):
            task13()
            self.assertEqual(mock_stdout.getvalue(), '0\n1\n')


    @patch('sys.stdout', new_callable=StringIO)
    def test6(self, mock_stdout):
        user_input = ['3 6', '0 7', '0 0', '2 0', '3 3', '4 0', '5 0']
        with patch('builtins.input', side_effect=user_input):
            task13()
            self.assertEqual(mock_stdout.getvalue(), '0\n7\n7\n-1\n-1\n-1\n')


    @patch('sys.stdout', new_callable=StringIO)
    def test7(self, mock_stdout):
        user_input = ['2 6', '0 2', '0 0', '2 0', '3 0', '4 0', '5 0']
        with patch('builtins.input', side_effect=user_input):
            task13()
            self.assertEqual(mock_stdout.getvalue(), '0\n2\n2\n3\n4\n5\n')


    @patch('sys.stdout', new_callable=StringIO)
    def test8(self, mock_stdout):
        user_input = ['1 25', '16 0', '29 3', '44 6', '58 0', '72 2', '88 8', '95 7', '108 6', '123 9', '139 6', '152 6', '157 3', '169 3', '183 1', '192 0', '202 8', '213 8', '229 3', '232 3', '236 3', '239 4', '247 8', '251 2', '267 7', '275 7']
        with patch('builtins.input', side_effect=user_input):
            task13()
            self.assertEqual(mock_stdout.getvalue(), '16\n29\n44\n58\n72\n88\n-1\n108\n123\n139\n152\n-1\n169\n183\n192\n202\n213\n229\n232\n236\n239\n247\n-1\n267\n275\n')


    @patch('sys.stdout', new_callable=StringIO)
    def test9(self, mock_stdout):
        user_input = ['11 25', '6 23', '15 44', '24 28', '25 15', '33 7', '47 41', '58 25', '65 5', '70 14', '79 8', '93 43', '103 11', '110 25', '123 27', '138 40', '144 19', '159 2', '167 23', '179 43', '182 31', '186 7', '198 16', '208 41', '222 23', '235 26']
        with patch('builtins.input', side_effect=user_input):
            task13()
            self.assertEqual(mock_stdout.getvalue(), '6\n29\n73\n101\n116\n123\n164\n189\n194\n208\n216\n259\n270\n295\n322\n362\n-1\n381\n-1\n-1\n-1\n404\n420\n461\n484\n')


    @patch('sys.stdout', new_callable=StringIO)
    def test10(self, mock_stdout):
        user_input = ['13 25', '10 37', '20 45', '29 24', '31 17', '38 43', '49 30', '59 12', '72 28', '82 45', '91 10', '107 46', '113 4', '128 16', '139 1', '149 41', '163 0', '172 22', '185 1', '191 17', '201 3', '209 11', '223 30', '236 17', '252 42', '262 0']
        with patch('builtins.input', side_effect=user_input):
            task13()
            self.assertEqual(mock_stdout.getvalue(), '10\n47\n92\n116\n133\n176\n206\n218\n246\n291\n301\n347\n351\n367\n368\n409\n409\n431\n-1\n-1\n432\n443\n-1\n473\n-1\n')


    @patch('sys.stdout', new_callable=StringIO)
    def test11(self, mock_stdout):
        user_input = ['12 25', '5 11', '10 14', '25 17', '41 22', '54 36', '70 13', '81 8', '90 12', '103 21', '115 38', '124 18', '138 15', '142 13', '155 31', '168 0', '177 49', '186 8', '196 30', '206 37', '217 49', '232 31', '247 25', '260 31', '268 36', '279 8']
        with patch('builtins.input', side_effect=user_input):
            task13()
            self.assertEqual(mock_stdout.getvalue(), '5\n16\n30\n47\n69\n105\n118\n126\n138\n159\n197\n215\n230\n243\n274\n274\n323\n331\n361\n398\n447\n478\n503\n534\n570\n')


    @patch('sys.stdout', new_callable=StringIO)
    def test12(self, mock_stdout):
        user_input = ['11 25', '11 45', '26 22', '38 24', '42 49', '48 39', '59 3', '67 1', '76 5', '84 30', '89 37', '99 12', '111 6', '125 33', '132 20', '147 16', '160 7', '174 15', '185 14', '198 9', '200 37', '208 18', '222 3', '237 28', '248 10', '263 11']
        with patch('builtins.input', side_effect=user_input):
            task13()
            self.assertEqual(mock_stdout.getvalue(), '11\n56\n78\n102\n151\n190\n193\n194\n199\n229\n266\n278\n284\n317\n-1\n337\n-1\n-1\n344\n353\n390\n408\n411\n-1\n-1\n')


    @patch('sys.stdout', new_callable=StringIO)
    def test13(self, mock_stdout):
        user_input = ['7 25', '0 21', '10 35', '10 12', '21 13', '35 11', '35 14', '51 49', '59 33', '59 43', '67 42', '80 14', '93 45', '93 38', '100 8', '101 31', '108 46', '123 22', '127 20', '139 7', '142 43', '142 12', '142 25', '154 25', '154 5', '154 42']
        with patch('builtins.input', side_effect=user_input):
            task13()
            self.assertEqual(mock_stdout.getvalue(), '0\n21\n56\n68\n81\n92\n106\n155\n188\n-1\n231\n245\n290\n-1\n-1\n328\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n')


    @patch('sys.stdout', new_callable=StringIO)
    def test14(self, mock_stdout):
        user_input = ['1 25', '15 23', '24 44', '39 43', '48 15', '56 6', '56 8', '56 29', '56 28', '56 4', '56 17', '68 44', '75 22', '75 34', '84 46', '84 21', '84 25', '97 31', '105 34', '105 43', '117 17', '129 12', '142 47', '144 22', '144 18', '152 9']
        with patch('builtins.input', side_effect=user_input):
            task13()
            self.assertEqual(mock_stdout.getvalue(), '15\n-1\n39\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n84\n-1\n-1\n-1\n-1\n-1\n-1\n-1\n142\n-1\n-1\n-1\n')


if __name__ == '__main__':
    unittest.main()