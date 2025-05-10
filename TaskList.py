from Task import Task

class TaskList:
    def __init__(self):
        self.__list_for_sort = []
        self.__tasks = []

    def add_task(self, task):
        """
        Додає завдання до списку завдань, якщо об'єкт є екземпляром класу Task.

        Метод перевіряє, чи переданий об'єкт є дійсним завданням (екземпляром Task),
        і у разі успіху додає його до внутрішнього списку. Якщо об'єкт не є завданням,
        виводиться повідомлення про помилку.

        Параметри:
        task : Task
            Об'єкт завдання, який потрібно додати до списку.
        """

        if isinstance(task, Task):
            self.__tasks.append(task)
            print(f"Завдання '{task.get_title()}' додано.")
        else:
            print("Завдання не додано. Переданий об'єкт не є завданням.")

    def delete_task(self, task_title):
        """
        Видаляє завдання зі списку за його назвою.

        Метод проходить по списку завдань і завдання, назва якого відповідає вказаному параметру.
        Якщо такого завдання не знайдено — виводиться відповідне повідомлення.

        Параметри:
        task_title : str
            Назва завдання, яке потрібно видалити.
        """

        for task in self.__tasks:
            if task.get_title() == task_title:
                self.__tasks.remove(task)
                print(f"Завдання '{task_title}' видалено.")
                return
        print(f"Завдання з назвою '{task_title}' не знайдено.")

    def mark_task_as_completed(self, task):
        """
        Позначає передане завдання як виконане.

        Метод перевіряє, чи присутнє завдання у списку,
        і змінює його статус на "Виконано". Якщо завдання не знайдено —
        виводиться відповідне повідомлення.

        Параметри:
        task : Task
            Об'єкт завдання, який потрібно позначити як виконаний.
        """

        if task in self.__tasks:
            task.set_status("Виконано")
            print(f"Завдання '{task.get_title()}' позначене як виконане.")
        else:
            print("Завдання не знайдено в списку.")

    def view_tasks(self, sort_by=None):
        """
        Виводить список завдань з можливістю сортування.

        Параметри:
        sort_by : str або None
            Критерій сортування ('date' або 'priority'). Якщо None — список не сортується.

        Сортує завдання за датою завершення або пріоритетом,
        залежно від значення параметра sort_by.
        Формат дати в завданнях має бути ДД.ММ.РРРР.
        """

        if not self.__tasks:
            print("Список завдань порожній.")
            return

        tasks_to_display = self.__tasks[:]

        match sort_by:
            case "date":
                print("Завдання відсортовані за датою:")
                tasks_to_display.sort(key=self.__get_end_date)
            case "priority":
                print("Завдання відсортованні за пріоритетом.")
                tasks_to_display.sort(key=self.__get_priority)

        for task in tasks_to_display:
            task.display()

    @staticmethod
    def __get_end_date(task_obj):
        return task_obj.get_end_date()

    @staticmethod
    def __get_priority(task_obj):
        return task_obj.get_priority()

if __name__ == '__main__':
    task1 = Task("Завдання 1", "Опис завдання 1", 4, "01.01.2025")
    task2 = Task("Завдання 2", "Опис завдання 2", 3, "12.12.2025")

    task_list = TaskList()
    task_list.add_task(task1)
    task_list.add_task(task2)

    task_list.view_tasks("priority")
