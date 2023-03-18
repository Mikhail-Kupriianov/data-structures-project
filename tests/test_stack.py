"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import pytest
from src.stack import Node, Stack


@pytest.fixture
def test_data():
    return [10, 'data', 'Test']


def test_node_init(test_data):
    n1 = Node(test_data[0])
    n2 = Node(test_data[1])
    assert n1.data == 10
    assert n2.data == 'data'


def test_pointer_node(test_data):
    n1 = Node(test_data[0])
    n2 = Node(test_data[1], n1)
    n3 = Node(test_data[2], n2)

    assert n1.next_node is None
    assert n2.next_node == n1
    assert n3.next_node == n2


def test_push(test_data):
    stack = Stack()
    for i in test_data:
        stack.push(i)
    assert stack.top.data == 'Test'
    assert stack.top.next_node.data == 'data'
    assert stack.top.next_node.next_node.data == 10
    assert stack.top.next_node.next_node.next_node is None