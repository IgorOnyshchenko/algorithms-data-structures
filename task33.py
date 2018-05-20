import unittest
from io import StringIO
from unittest.mock import patch


class RollingHash:
    def __init__(self, text, sizeWord):
        self.text = text
        self.hash = 0
        self.sizeWord = sizeWord

        for i in range(0, sizeWord):
            #ord maps the character to a number
            #subtract out the ASCII value of "a" to start the indexing at zero
            self.hash += (ord(self.text[i]) - ord("a")+1)*(26**(sizeWord - i -1))

        #start index of current window
        self.window_start = 0
        #end of index window
        self.window_end = sizeWord

    def move_window(self):
        if self.window_end <= len(self.text) - 1:
            #remove left letter from hash value
            self.hash -= (ord(self.text[self.window_start]) - ord("a")+1)*26**(self.sizeWord-1)
            self.hash *= 26
            self.hash += ord(self.text[self.window_end])- ord("a")+1
            self.window_start += 1
            self.window_end += 1

    def window_text(self):
        return self.text[self.window_start:self.window_end]

def task33():
    word = input()
    text = input()

    if word == "" or text == "":
        return None
    if len(word) > len(text):
        return None

    rolling_hash = RollingHash(text, len(word))
    word_hash = RollingHash(word, len(word))

    for i in range(len(text) - len(word) + 1):
        if rolling_hash.hash == word_hash.hash:
            if rolling_hash.window_text() == word:
                print(i, end=' ')
        rolling_hash.move_window()
    return None


def task33_():
    pattern = input()
    text = input()

    p = 31
    p_pow = [1]*max(len(pattern), len(text))
    for i in range(1, len(p_pow)):
        p_pow[i] = p_pow[i-1] * p

    h = [1]*len(text)
    h[0] = ord(text[0]) - ord('a') + 1
    for i in range(1, len(text)):
        h[i] = (ord(text[i]) - ord('a') + 1) * p_pow[i] + h[i-1]

    h_s = 0
    for i in range(len(pattern)):
        h_s += (ord(pattern[i]) - ord('a') + 1) * p_pow[i]

    for i in range(len(text) - len(pattern) + 1):
        cur_h = h[i+len(pattern)-1]
        if i:
            cur_h -= h[i-1]
        # print(cur_h, h_s)
        if cur_h == h_s * p_pow[i]:
            print(i, end=' ')


class Task33TestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test1(self, mock_stdout):
        user_input = ['aba', 'abacaba']
        with patch('builtins.input', side_effect=user_input):
            task33()
            self.assertEqual(mock_stdout.getvalue(), '0 4 ')

    @patch('sys.stdout', new_callable=StringIO)
    def test2(self, mock_stdout):
        user_input = ['Test', 'testTesttesT']
        with patch('builtins.input', side_effect=user_input):
            task33()
            self.assertEqual(mock_stdout.getvalue(), '4 ')

    @patch('sys.stdout', new_callable=StringIO)
    def test3(self, mock_stdout):
        user_input = ['aaaaa', 'baaaaaaa']
        with patch('builtins.input', side_effect=user_input):
            task33()
            self.assertEqual(mock_stdout.getvalue(), '1 2 3 ')


if __name__ == '__main__':
    unittest.main()