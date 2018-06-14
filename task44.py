import unittest
from io import StringIO
from unittest.mock import patch


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.size = 1
        self.sum = key
        # self.parent = None


class AVL:
    @staticmethod
    def insert(root: Node, key: int) -> Node:
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = AVL.insert(root.left, key)
        else:
            root.right = AVL.insert(root.right, key)
        return AVL.balance(root)

    @staticmethod
    def remove(root: Node, key: int) -> Node:
        if root is None:
            return None
        if key < root.key:
            root.left = AVL.remove(root.left, key)
        elif key > root.key:
            root.right = AVL.remove(root.right, key)
        else:
            l = root.left
            r = root.right
            if l is None:
                return r
            max_node = AVL.findmax(l)
            max_node.left = AVL.removemax(l)
            max_node.right = r
            return AVL.balance(max_node)
        return AVL.balance(root)

    @staticmethod
    def find(root: Node, key: int) -> bool:
        if root is None:
            return False
        if key < root.key:
            return AVL.find(root.left, key)
        elif key > root.key:
            return AVL.find(root.right, key)
        else:
            return True

    @staticmethod
    def merge(v1, v2) -> Node:
        if v1 is None:
            return v2
        elif v2 is None:
            return v1
        T = AVL.findmax(v1)
        v1 = AVL.removemax(v1)
        return AVL.avl_merge_with_root(v1, v2, T)

    @staticmethod
    def split(root: Node, key: int) -> tuple:
        if root is None:
            return (None, None)
        if key < root.key:
            left_split = AVL.split(root.left, key)
            right_tree = AVL.avl_merge_with_root(left_split[1], root.right, root)
            return (left_split[0], right_tree)
        else:
            right_split = AVL.split(root.right, key)
            left_tree = AVL.avl_merge_with_root(root.left, right_split[0], root)
            return (left_tree, right_split[1])

    @staticmethod
    def sum_less_than(root: Node, key: int) -> bool:
        if root is None:
            return 0
        if key < root.key:
            return 0 + AVL.sum_less_than(root.left, key)
        elif key > root.key:
            return (root.left.sum if root.left is not None else 0) + root.key + AVL.sum_less_than(root.right, key)
        else:
            return root.left.sum if root.left is not None else 0

    @staticmethod
    def sum_greater_than(root: Node, key: int) -> bool:
        if root is None:
            return 0
        if key < root.key:
            return (root.right.sum if root.right is not None else 0) + root.key + AVL.sum_greater_than(root.left, key)
        elif key > root.key:
            return 0 + AVL.sum_greater_than(root.right, key)
        else:
            return root.right.sum if root.right is not None else 0

    @staticmethod
    def sum_modified(root: Node, l: int, r: int) -> int:
        if root is None:
            return 0
        return max(root.sum - AVL.sum_less_than(root, l) - AVL.sum_greater_than(root, r), 0)

    @staticmethod
    def sum(root: Node, l: int, r: int) -> tuple:
        split1 = AVL.split(root, max(l-1, 0))
        split2 = AVL.split(split1[1], r)
        lr_sum = AVL.get_sum(split2[0])
        root = AVL.merge(split1[0], AVL.merge(split2[0], split2[1]))
        return lr_sum, root

    @staticmethod
    def merge_with_root(v1: Node, v2: Node, T: Node) -> Node:
        T.left = v1
        T.right = v2
        return T

    @staticmethod
    def avl_merge_with_root(v1: Node, v2: Node, T: Node) -> Node:
        if abs(AVL.get_height(v1) - AVL.get_height(v2)) <= 1:
            merged = AVL.merge_with_root(v1, v2, T)
            AVL.update(merged)
            # return AVL.balance(merged)
            return merged
        elif AVL.get_height(v1) > AVL.get_height(v2):
            right_merged = AVL.avl_merge_with_root(v1.right, v2, T)
            v1.right = right_merged
            # right_merged.parent = v1
            return AVL.balance(v1)
        else:
            left_merged = AVL.avl_merge_with_root(v1, v2.left, T)
            v2.left = left_merged
            # left_merged.parent = v2
            return AVL.balance(v2)

    @staticmethod
    def findmax(root: Node) -> Node:
        return AVL.findmax(root.right) if root.right is not None else root

    @staticmethod
    def removemax(root: Node) -> Node:
        if root.right is None:
            return root.left
        root.right = AVL.removemax(root.right)
        return AVL.balance(root)

    @staticmethod
    def get_height(root: Node) -> int:
        return root.height if root is not None else 0

    @staticmethod
    def get_size(root: Node) -> int:
        return root.size if root is not None else 0

    @staticmethod
    def get_sum(root: Node) -> int:
        return root.sum if root is not None else 0

    # должен быть -1, 0 или 1
    # если -2 или 2, то нужно применять повороты
    @staticmethod
    def get_balance_factor(root: Node) -> int:
        return AVL.get_height(root.right) - AVL.get_height(root.left)

    @staticmethod
    def update(root: Node) -> None:
        root.height = max(AVL.get_height(root.right), AVL.get_height(root.left)) + 1
        root.size = AVL.get_size(root.left) + AVL.get_size(root.right) + 1
        root.sum = AVL.get_sum(root.right) + AVL.get_sum(root.left) + root.key

    @staticmethod
    def rotate_right(root: Node) -> Node:
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        AVL.update(root)
        AVL.update(new_root)
        return new_root

    @staticmethod
    def rotate_left(root: Node) -> Node:
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        AVL.update(root)
        AVL.update(new_root)
        return new_root

    @staticmethod
    def balance(root: Node) -> Node:
        AVL.update(root)
        if AVL.get_balance_factor(root) == 2:
            if AVL.get_balance_factor(root.right) < 0:
                root.right = AVL.rotate_right(root.right)
            return AVL.rotate_left(root)
        if AVL.get_balance_factor(root) == -2:
            if AVL.get_balance_factor(root.left) < 0:
                root.left = AVL.rotate_right(root.left)
            return AVL.rotate_right(root)
        return root

    @staticmethod
    def walk(root: Node):
        if root is None:
            return
        AVL.walk(root.left)
        print(root.key, end=' ')
        AVL.walk(root.right)



def task44():
    def f(x):
        return (x+s) % 1000000001

    n, s, root = int(input()), 0, None
    for _ in range(n):
        line = input().split()
        if line[0] == '+':
            value = f(int(line[1]))
            if not AVL.find(root, value):
                root = AVL.insert(root ,value)
        elif line[0] == '-':
            value = f(int(line[1]))
            if AVL.find(root, value):
                root = AVL.remove(root ,value)
        elif line[0] == '?':
            value = f(int(line[1]))
            print('Found' if AVL.find(root, value) else 'Not found')
        elif line[0] == 's':
            left, right = f(int(line[1])), f(int(line[2]))
            s = AVL.sum_modified(root, left, right)
            print(s)


class Task44TestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test1(self, mock_stdout):
        user_input = ['15', '? 1', '+ 1', '? 1', '+ 2', 's 1 2', '+ 1000000000', '? 1000000000', '- 1000000000', '? 1000000000', 's 999999999 1000000000', '- 2', '? 2', '- 0', '+ 9', 's 0 9']
        with patch('builtins.input', side_effect=user_input):
            task44()
            self.assertEqual(mock_stdout.getvalue(), 'Not found\nFound\n3\nFound\nNot found\n1\nNot found\n10\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test2(self, mock_stdout):
        user_input = ['5', '? 0', '+ 0', '? 0', '- 0', '? 0']
        with patch('builtins.input', side_effect=user_input):
            task44()
            self.assertEqual(mock_stdout.getvalue(), 'Not found\nFound\nNot found\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test3(self, mock_stdout):
        user_input = ['5', '+ 491572259', '? 491572259', '? 899375874', 's 310971296 877523306', '+ 352411209']
        with patch('builtins.input', side_effect=user_input):
            task44()
            self.assertEqual(mock_stdout.getvalue(), 'Found\nNot found\n491572259\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test4(self, mock_stdout):
        user_input = ['96', 's 40279559 89162572', '- 774613289', 's 869592654 915517087', '- 165280355', '- 776346290', '- 221187096', 's 421986248 742826969', 's 83228103 852190011', '- 640319482', '? 528689193', '? 75245219', '- 617070033', '+ 66257759', 's 25751289 70170547', 's 28248247 617849094', '- 954357244', '+ 477444954', '? 608389416', 's 400483980 423330836', '- 477444954', '? 441393551', 's 66257759 66257759', '- 822218158', '? 806479414', 's 548665149 925635534', 's 66257759 66257759', '? 234121006', '+ 663305907', 's 314809050 685231317', '- 0', 's 487458874 602635501', 's 66257759 66257759', '? 918193520', '? 606474691', 's 188185089 774086933', '- 322445571', 's 66257759 66257759', '- 814123984', 's 0 0', 's 0 0', 's 689260392 827869844', '? 204276815', '- 66257759', '? 488766408', 's 412617563 631410280', '- 463415495', '+ 601030115', '? 776513589', 's 257003372 887483600', '+ 154047223', '? 154047223', '? 219327735', '+ 978812473', 's 978812473 154047223', '? 718062555', '? 128066784', '- 15718305', '? 754978417', 's 643892549 819127300', '? 192401474', '? 643892549', '+ 638898307', '? 973173529', '+ 506709268', '- 506709268', '+ 744166533', '- 638898307', '+ 95240753', 's 997348833 63778002', '? 31190791', 's 21011834 570648768', '+ 217208615', '+ 401912531', 's 0 723886547', '? 251082460', '+ 542593404', 's 702430665 542593404', '? 48285749', 's 831077135 671239874', '+ 917941607', '? 908494561', '? 671239874', 's 333354822 490605331', '+ 261522346', 's 170201520 10364259', '- 139162050', '- 677374727', '? 992422786', '? 500171144', '- 239436034', '+ 556867643', '? 992422786', '+ 720003678', 's 220110584 268880636', 's 31190791 997548180', 's 898610232 383552107']
        with patch('builtins.input', side_effect=user_input):
            task44()
            self.assertEqual(mock_stdout.getvalue(), '0\n0\n0\n0\nNot found\nNot found\n66257759\n0\nNot found\n0\nNot found\n66257759\nNot found\n0\n66257759\nNot found\n729563666\n0\n66257759\nNot found\nNot found\n0\n66257759\n66257759\n66257759\n0\nNot found\nNot found\n0\nNot found\n601030115\nFound\nNot found\n1935950040\nNot found\nNot found\nNot found\n1935950040\nNot found\nFound\nNot found\n0\nFound\n31190791\n3328760130\nFound\n4200113661\nFound\n4200113661\nNot found\nFound\n1860989273\n4440680541\nFound\nNot found\nFound\n0\n4220898514\n1565728674\n')


if __name__ == '__main__':
    unittest.main()