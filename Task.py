from datetime import date

class Task:
    def __init__(self, title, description, priority, end_date, status="Не виконано"):
        if not self.validate(end_date, description, priority, status):
            raise ValueError("Завдання не створено.")

        self.__title = title
        self.__description = description
        self.__priority = priority
        self.__end_date = datetime.strptime(end_date, "%d.%m.%Y").date()
        self.__status = status

        if description_validation == description and date_validation == end_date and priority_validation == priority:
            self.title = title
            self.description = description
            self.priority = priority_validation
            self.end_date = end_date
            self.status = status
        else:
            print("Завдання не створено.")
            if description_validation != description:
                print(description_validation)
            if date_validation != end_date:
                print(date_validation)
            if priority_validation != priority:
                print(priority_validation)


    @staticmethod
    def __validate_date(date_string):
        if type(date_string) is not str:
            return 'Дата повинна бути рядковим значенням.'
        if not date_string:
            return 'Значення дати не може бути пустим.'

        parts = date_string.split('.')

        if len(parts) != 3:
            return "Дата повинна бути у форматі ДД.ММ.РРРР"

        if not parts[0].isdigit():
            return "День повинен бути числом."
        if not parts[1].isdigit():
            return "Місяць повинен бути числом."
        if not parts[2].isdigit():
            return "Рік повинен бути числом."

        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])

        if not (1 <= month <= 12):
            return "У році є тільки 12 місяців"

        max_days = 0

        if month in [1, 3, 5, 7, 8, 10, 12]:
            max_days = 31
        elif month in [4, 6, 9, 11]:
            max_days = 30
        elif month == 2:
            max_days = 29

        if day > max_days:
            return f"У вказаному місяці є тільки {max_days} днів."

        current_year = date.today().year
        if year < current_year:
            return "Рік закінчення завдання не може бути меншим ніж теперішній"

        if year > (current_year + 15):
            return "Дата завершення завдання не може перевищувати 15 років від його створення."

        return date_string

    @staticmethod
    def __validate_description(description):
        if not description:
            return "Не введено опис завдання."
        if len(description) > 255:
            return 'Довжина опису не повинна перевищувати 255 символів. '
        return description

    @staticmethod
    def __get_priorities():
        repriorities = {
            1: 'Низький',
            2: 'Середній',
            3: 'Високий',
            4: 'Терміновий',
            5: 'Критичний'
        }
        return repriorities

    @staticmethod
    def __validate_priority(priority):
        priorities = Task.__get_priorities()
        if not priority:
            return "Не встановлене значення пріоритету."

        if isinstance(priority, int):
            if priority in priorities:
                return priorities[priority]
            else:
                return "Пріоритет повинен бути числом від 1 до 5."

        if isinstance(priority, str):
            priority = priority.lower()
            for key, value in priorities.items():
                if priority == value.lower():
                    return value
            return "Введений пріоритет не є допустимим."

        return "Пріоритет повинен бути цілим числом або одним із допустимих значень."



if __name__ == '__main__':
    task = Task("Лалал", "Опа", 5,"11.11.2025", "<UNK>")
    print(task.title)
    print(task.priority)
    print(task.description)
    print(task.end_date)
    print(task.status)