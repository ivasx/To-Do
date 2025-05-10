from TaskList import TaskList


class TaskManager:
    def __init__(self):
        self.__lists = {}

    def create_list(self, list_name):
        if list_name in self.__lists:
            print(f"Список '{list_name}' вже існує.")
        else:
            self.__lists[list_name] = TaskList()
            print(f"Список '{list_name}' створено.")

    def get_list(self, list_name):
        return self.__lists.get(list_name, None)

    def delete_list(self, list_name):
        if list_name in self.__lists:
            del self.__lists[list_name]
            print(f"Список '{list_name}' видалено.")
        else:
            print(f"Список '{list_name}' не знайдено.")
