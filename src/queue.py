class Node:
    """Класс для узла очереди"""

    def __init__(self, data=None, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        stack_content = ""
        current_node = self.head
        while current_node is not None:
            stack_content += str(current_node.data) + "\n"
            current_node = current_node.next_node
        return stack_content[:-1]

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        del_data = self.head.data
        self.head = self.head.next_node
        return del_data


# if __name__ == '__main__':
#     queue = Queue()
#
#     # Магический метод __str__ возвращает пустую строку
#     print('assert str(Queue()) == "" -> ', str(Queue()))
#
#     queue.enqueue('data1')
#     queue.enqueue('data2')
#     queue.enqueue('data3')
#
#     print("assert queue.head.data == 'data1' -> ", str(queue.head.data))
#     print("assert queue.head.next_node.data == 'data2' -> ", str(queue.head.next_node.data))
