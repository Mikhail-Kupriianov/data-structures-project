class Node:
    """Класс для узла стека"""

    def __init__(self, data=None, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node

    def __del__(self):
        print("Удаляется", self.__class__.__name__, self.data)


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def push(self, data) -> None:
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        new_node = Node(data)
        if self.top:
            new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        del_data = self.top.data
        self.top = self.top.next_node
        return del_data

    def __str__(self):
        return f"{self.__class__.__name__} - {self.top.data}"


if __name__ == '__main__':
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    print(str(stack))
