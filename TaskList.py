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

    def filter_tasks(self, filter_by=None, filter_value=None):
        """
        Виводить завдання, що відповідають заданому критерію фільтрації.

        Метод дозволяє фільтрувати завдання за статусом або пріоритетом.
        Якщо вказано неправильний параметр фільтрації, виводиться повідомлення про помилку.

        Параметри:
        filter_by : str або None
            Критерій фільтрації ('status' або 'priority').
        filter_value : str або int або None
            Значення, за яким здійснюється фільтрація:
            - для 'status' — рядок (наприклад, "Виконано"),
            - для 'priority' — ціле число (наприклад, 3).

        Приклад використання:
        filter_tasks("status", "Виконано")
        filter_tasks("priority", 2)
        """

        match filter_by:
            case "status":
                print(f"Завдання відфільтровані за статусом {filter_value}:")
                for task in self.__tasks:
                    if task.get_status() == filter_value:
                        task.display()
            case "priority":
                print(f"Завдання відфільтровані за пріоритетом {filter_value}:")
                for task in self.__tasks:
                    if task.get_priority() == filter_value:
                        task.display()
            case _:
                print("Введено неправильний параметр для фільтрації.")

    def change_task(self, title, new_description=None, new_date=None, new_priority=None):
        """
        Оновлює інформацію про завдання за назвою.

        Параметри:
        title : str
            Назва завдання, яке потрібно оновити.
        new_description : str або None
            Новий опис завдання.
        new_date : str або None
            Нова дата завершення (у форматі ДД.ММ.РРРР).
        new_priority : int або None
            Новий пріоритет (ціле число).
        """

        for task in self.__tasks:
            if task.get_title() == title:
                if new_description is not None:
                    task.set_description(new_description)
                if new_date is not None:
                    task.set_end_date(new_date)
                if new_priority:
                    if new_priority.isdigit():
                        new_priority_val = int(new_priority)
                        if 1 <= new_priority_val <= 5:
                            task.set_priority(new_priority_val)
                        else:
                            print("Пріоритет має бути від 1 до 5. Значення не змінено.")
                    else:
                        print("Пріоритет повинен бути числом. Значення не змінено.")

                print(f"Завдання '{title}' оновлено.")
                return

        print(f"Завдання з назвою '{title}' не знайдено.")

    @staticmethod
    def __get_end_date(task_obj):
        return task_obj.get_end_date()

    @staticmethod
    def __get_priority(task_obj):
        return task_obj.get_priority()

    def get_task_by_title(self, task_title):
        """
        Повертає завдання за його назвою.

        Параметри:
        task_title : str
            Назва завдання, яке потрібно знайти.

        Повертає:
        Task або None
            Завдання, якщо знайдено, або None, якщо не знайдено.
        """
        for task in self.__tasks:
            if task.get_title() == task_title:
                return task
        return None

