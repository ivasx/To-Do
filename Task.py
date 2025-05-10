from datetime import date, datetime


class Task:
    def __init__(self, title, description, priority, end_date, status="Не виконано"):
        if not self.validate(end_date, description, priority, status):
            raise ValueError("Завдання не створено.")

        self.__title = title
        self.__description = description
        self.__priority = priority
        self.__end_date = datetime.strptime(end_date, "%d.%m.%Y").date()
        self.__status = status

    @classmethod
    def validate(cls, date_string, description, priority, status="Не виконано"):
        """
        Перевіряє коректність введених даних для завдання (дату, опис, пріоритет).

        Параметри:
        ----------
        date_string : str
            Дата у форматі "ДД.ММ.РРРР".

        description : str
            Опис завдання (макс. 255 символів).

        priority : int
            Пріоритет завдання (від 1 до 5).

        Повертає:
        ---------
        bool
            `True`, якщо всі перевірки пройдені успішно, і `False` в іншому випадку.
        """

        return (
                cls.__validate_date(date_string)
                and cls.__validate_description(description)
                and cls.__validate_priority(priority)
                and cls.__validate_status(status)
        )

    #Перевірка коректності введення дати
    @staticmethod
    def __validate_date(date_string):
        """
        Функція перевіряє, чи є введена дата рядковим значенням, чи не є вона порожньою,
        чи правильно зазначені день, місяць і рік, а також чи відповідає дата реальним
        можливим значенням для кожного місяця. Також перевіряється, чи не є рік
        меншим за поточний і чи не перевищує він межу в 15 років від поточного року.

        Параметри:
        ----------
        date_string : str
            Дата у форматі "ДД.ММ.РРРР".

        Повертає:
        ---------
        bool
            `True`, якщо дата є коректною, і `False`, якщо дата неправильна.
        """

        if type(date_string) is not str:
            print("Дата повинна бути рядковим значенням.")
            return False
        if not date_string:
            print("Значення дати не може бути пустим.")
            return False

        parts = date_string.split('.')

        if len(parts) != 3:
            print("Дата повинна бути у форматі ДД.ММ.РРРР")
            return False

        if not parts[0].isdigit():
            print("День повинен бути числом.")
            return False
        if not parts[1].isdigit():
            print("Місяць повинен бути числом.")
            return False
        if not parts[2].isdigit():
            print("Рік повинен бути числом.")
            return False

        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])

        if not (1 <= month <= 12):
            print("У році є тільки 12 місяців")
            return False

        max_days = 0

        if month in [1, 3, 5, 7, 8, 10, 12]:
            max_days = 31
        elif month in [4, 6, 9, 11]:
            max_days = 30
        elif month == 2:
            max_days = 29

        if day > max_days:
            print(f"У вказаному місяці є тільки {max_days} днів.")
            return False

        current_year = date.today().year
        if year < current_year:
            print("Рік закінчення завдання не може бути меншим ніж теперішній")
            return False

        if year > (current_year + 15):
            print("Дата завершення завдання не може перевищувати 15 років від його створення.")
            return False

        return True

    # Перевірка наявності опису завдання
    # та обмеження на довжину опису завдання
    @staticmethod
    def __validate_description(description):
        """
        Перевіряє коректність опису завдання. Метод перевіряє наявність
        завдання та виконує обмеження на довжину тексту завдання.

        Параметри:
        description : str
            Опис завдання.

        Повертає:
        bool
            `True`, якщо опис не порожній і його довжина не перевищує 255 символів, інакше `False`.
        """

        if not description:
            print("Не введено опис завдання.")
            return False
        if len(description) > 255:
            print("Довжина опису не повинна перевищувати 255 символів. ")
            return False
        return True

    # Перевірка коректності пріоритету
    @staticmethod
    def __validate_priority(priority):
        """
        Перевіряє коректність пріоритету завдання.

        Пріоритет визначає важливість завдання та повинен бути цілим числом
        у діапазоні від 1 (найнижчий) до 5 (найвищий). Метод перевіряє, чи
        передане значення є числом та чи входить у допустимий діапазон.

        Параметри:
        priority : int
            Значення пріоритету.

        Повертає:
        bool
            `True`, якщо пріоритет є цілим числом від 1 до 5 включно, інакше `False`.
        """

        if not isinstance(priority, int):
            print("Пріоритет повинен бути числом.")
            return False
        if priority < 1 or priority > 5:
            print("Пріоритет повинен бути числом від 1 до 5.")
            return False
        return True

    @staticmethod
    def __validate_status(status):
        if not status in ["Не виконано", "Виконано"]:
            print("Невірний статус. Можливі значення: 'Виконано', 'Не виконано'.")
            return False
        else:
            return True

    def display(self):
        print(f"Завдання: {self.get_title()}, Дата завершення: {self.get_end_date()}, Пріоритет: {self.get_priority()}")
    # Геттери і сеттери
    def get_title(self):
        return self.__title

    def set_title(self, title):
        if title:
            self.__title = title

    def get_description(self):
        return self.__description

    def set_description(self, description):
        if self.__validate_description(description):
            self.__description = description

    def get_priority(self):
        return self.__priority

    def set_priority(self, priority):
        if self.__validate_priority(priority):
            self.__priority = priority

    def get_end_date(self):
        return self.__end_date

    def set_end_date(self, end_date):
        if self.__validate_date(end_date):
            self.__end_date = datetime.strptime(end_date, "%d.%m.%Y").date()

    def get_status(self):
        return self.__status

    def set_status(self, status):
        if self.__validate_status(status):
            self.__status = status





if __name__ == '__main__':
    task = Task("Лалал", "Опа", 4,"11.11.2025")
    print(task)
    print(task.validate("11.11.2025", "Опа", 4))
