"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Node, Queue


class TestQueue(unittest.TestCase):

    def test_node_init(self):
        n1 = Node(10)
        n2 = Node('data', n1)
        self.assertEqual(n1.data, 10)
        self.assertEqual(n2.data, 'data')
        self.assertEqual(n2.next_node, n1)

    def test_queue_init(self):
        queue = Queue()
        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)

    def test_queue_str(self):
        queue = Queue()
        self.assertEqual(str(Queue()), "")
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(str(queue), "data1\ndata2\ndata3")

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.next_node.data, 'data2')
        self.assertEqual(queue.tail.data, 'data3')
        self.assertIsNone(queue.tail.next_node)

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        data = queue.dequeue()

        self.assertEqual(data, 'data1')
        self.assertEqual(str(queue), "data2\ndata3")
        self.assertEqual(queue.head.data, "data2")
        self.assertEqual(queue.tail.data, "data3")


if __name__ == '__main__':
    unittest.main()
