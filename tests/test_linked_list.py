"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import Node, LinkedList


class TestLinkedList(unittest.TestCase):

    def test_node_init(self):
        n1 = Node({'id': 0})
        n2 = Node({'id': 1}, n1)
        self.assertEqual(n1.data, {'id': 0})
        self.assertEqual(n2.data, {'id': 1})
        self.assertEqual(n2.next_node, n1)

    def test_linkedlist_init(self):
        ll = LinkedList()
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

    def test_linkedlist_str(self):
        ll = LinkedList()
        self.assertEqual(str(ll), 'None')
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        self.assertEqual(str(ll), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")

    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 0})
        ll.insert_beginning({'id': 1})
        ll.insert_beginning({'id': 2})
        self.assertEqual(ll.head.data, {'id': 2})
        self.assertEqual(ll.head.next_node.data, {'id': 1})
        self.assertEqual(ll.tail.data, {'id': 0})
        self.assertIsNone(ll.tail.next_node)
        ll.insert_beginning(['id', 2])
        self.assertNotEquals(ll.head.data, ['id', 2])
        ll.insert_beginning({'id': -3})
        self.assertNotEquals(ll.head.data, {'id': -3})
        ll.insert_beginning({'i': 3})
        self.assertNotEquals(ll.head.data, {'i': 3})
        ll.insert_beginning({'id': 1.5})
        self.assertNotEquals(ll.head.data, {'id': 1.5})

    def test_insert_at_end(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 0})
        ll.insert_at_end({'id': 1})
        ll.insert_at_end({'id': 2})
        self.assertEqual(ll.head.data, {'id': 0})
        self.assertEqual(ll.head.next_node.data, {'id': 1})
        self.assertEqual(ll.tail.data, {'id': 2})
        self.assertIsNone(ll.tail.next_node)
        ll.insert_at_end({'id': 1.5})
        self.assertNotEquals(ll.head.data, {'id': 1.5})

    def test_to_list(self):
        ll = LinkedList()

        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})

        lst = ll.to_list()

        self.assertEqual(len(lst), 4)
        self.assertEqual(lst[2], {'id': 2, 'username': 'mik.roz'})
        self.assertEqual(lst[-1], {'id': 3, 'username': 'mosh_s'})

    def test_get_data_by_id(self):
        ll = LinkedList()

        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})

        lst = ll.to_list()

        self.assertEqual(ll.get_data_by_id(2), {'id': 2, 'username': 'mik.roz'})
        self.assertEqual(ll.get_data_by_id('2'), {})
        self.assertEqual(ll.get_data_by_id(1.5), {})
        self.assertEqual(ll.get_data_by_id(-3), {})
        self.assertEqual(ll.get_data_by_id(4), {})


if __name__ == '__main__':
    unittest.main()
