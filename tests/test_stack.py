"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

# import src.stack
# import pytest
from src.stack import Node, Stack


# @pytest.fixture
# def test_data():
#     return [10, 'data', 'Test']

class TestStack(unittest.TestCase):

    def test_node_init(self):
        n1 = Node(10)
        n2 = Node('data', n1)
        self.assertEqual(n1.data, 10)
        self.assertEqual(n2.data, 'data')
        self.assertEqual(n2.next_node, n1)

    # def test_node_init(test_data):
    #     n1 = Node(test_data[0])
    #     n2 = Node(test_data[1])
    #     assert n1.data == 10
    #     assert n2.data == 'data'

    # def test_pointer_node(test_data):
    #     n1 = Node(test_data[0])
    #     n2 = Node(test_data[1], n1)
    #     n3 = Node(test_data[2], n2)

    # assert n1.next_node is None
    # assert n2.next_node == n1
    # assert n3.next_node == n2

    def test_push(self):
        stack = Stack()
        stack.push(10)
        stack.push('data')
        stack.push('Test')
        self.assertEqual(stack.top.data, 'Test')
        self.assertEqual(stack.top.next_node.data, 'data')
        self.assertEqual(stack.top.next_node.next_node.data, 10)
        self.assertEqual(stack.top.next_node.next_node.next_node, None)

    # for i in test_data:
    #
    # assert stack.top.data == 'Test'
    # assert stack.top.next_node.data == 'data'
    # assert stack.top.next_node.next_node.data == 10
    # assert stack.top.next_node.next_node.next_node is None

    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        data = stack.pop()
        self.assertEqual(stack.top.data, 'data1')
        self.assertEqual(data, 'data2')
        data1 = stack.pop()
        self.assertEqual(stack.top, None)
        self.assertEqual(data1, 'data1')


if __name__ == '__main__':
    unittest.main()
