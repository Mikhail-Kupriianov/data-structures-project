class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data=None, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    @staticmethod
    def is_data_right_dict(data) -> bool:
        """
        Проверяет данные для односвязного списка.
        Правильные данные должны быть словарём, который содержит ключ "id" с целым, неотрицательным значением.
        """

        result = True
        if not isinstance(data, dict):
            result = False
        elif 'id' not in list(data.keys()):
            result = False
        elif not isinstance(data['id'], int):
            result = False
        elif data['id'] < 0:
            result = False
        return result

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if LinkedList.is_data_right_dict(data):

            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next_node = self.head
                self.head = new_node

        else:
            print('Данные не являются словарем или в словаре нет id.')

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        if LinkedList.is_data_right_dict(data):

            new_node = Node(data)
            if self.tail is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next_node = new_node
                self.tail = new_node

        else:
            print('Данные не являются словарем или в словаре нет id.')

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ""
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self) -> list:
        """Возвращает список с данными, содержащимися в односвязном списке `LinkedList`"""
        node = self.head
        result = []

        while node:
            result.append(node.data)
            node = node.next_node

        return result

    def get_data_by_id(self, id_dict: int) -> dict:
        try:
            if id_dict >= 0:
                test = id_dict
            else:
                test = 'tst'
            range(test)

        except TypeError:
            print('id должно быть целым, неотрицательным числом')
            return {}

        node = self.head

        while node:
            if list(node.data.values())[0] == int(id_dict):
                return node.data
            node = node.next_node
        print(f"'id': {id_dict} нет в списке")
        return {}


if __name__ == '__main__':
    """Код для тестирования модуля linked_list.py"""
    # # Создаем и наполняем односвязный список
    # ll = LinkedList()
    #
    # ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    # ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
    # ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
    # ll.insert_beginning({'id': 0, 'username': 'serebro'})
    #
    # # метод to_list()
    # lst = ll.to_list()
    # for item in lst:
    #     print(item)
    # # {'id': 0, 'username': 'serebro'}
    # # {'id': 1, 'username': 'lazzy508509'}
    # # {'id': 2, 'username': 'mik.roz'}
    # # {'id': 3, 'username': 'mosh_s'}
    #
    # # метод get_data_by_id()
    # user_data = ll.get_data_by_id(3)
    # assert user_data == {'id': 3, 'username': 'mosh_s'}
    #
    # # работа блока try/except
    # ll = LinkedList()
    # ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    # ll.insert_at_end('idusername')
    # ll.insert_at_end([1, 2, 3])
    # ll.insert_at_end({'id': 2, 'username': 'mosh_s'})
    #
    # user_data = ll.get_data_by_id(2)
    # # Данные не являются словарем или в словаре нет id.
    # # Данные не являются словарем или в словаре нет id.
    # print(user_data)
    # # {'id': 2, 'username': 'mosh_s'}
    # print("\nЧЕТЫРЕ РАЗА ВСТАВЛЯЕМ НЕПРАВИЛЬНЫЙ СЛОВАРЬ В СПИСОК\n")
    # ll.insert_at_end({'identification': 2, 'username': 'mosh_s'})
    # ll.insert_at_end({'id': 2.5, 'username': 'mosh_s'})
    # ll.insert_at_end({'id': 'id 1', 'username': 'mosh_s'})
    # ll.insert_at_end({'id': -2, 'username': 'mosh_s'})
    # print("\nЧЕТЫРЕ РАЗА ПЫТАЕМСЯ ПОЛУЧИТЬ СЛОВАРЬ ИЗ СПИСКА ПО НЕПРАВИЛЬНОМУ 'id'\n")
    # print(ll.get_data_by_id("stop"))
    # print(ll.get_data_by_id(1.5))
    # print(ll.get_data_by_id(-3))
    # print(ll.get_data_by_id(3))
