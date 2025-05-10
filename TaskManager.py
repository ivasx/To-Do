from TaskList import TaskList


class TaskManager:
    def __init__(self):
        self.__lists = {}

    def create_list(self, list_name):
        """
        Створює новий список завдань з вказаною назвою.

        Якщо список з такою назвою вже існує — виводиться відповідне повідомлення.

        Параметри:
        list_name : str
            Назва списку, який потрібно створити.
        """

        if list_name in self.__lists:
            print(f"Список '{list_name}' вже існує.")
        else:
            self.__lists[list_name] = TaskList()
            print(f"Список '{list_name}' створено.")

    def get_list(self, list_name):
        return self.__lists.get(list_name, None)

    def delete_list(self, list_name):
        """
        Видаляє список завдань за вказаною назвою.

        Якщо список не існує — виводиться повідомлення про помилку.

        Параметри:
        list_name : str
            Назва списку, який потрібно видалити.
        """

        if list_name in self.__lists:
            del self.__lists[list_name]
            print(f"Список '{list_name}' видалено.")
        else:
            print(f"Список '{list_name}' не знайдено.")
