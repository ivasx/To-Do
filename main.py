from TaskManager import TaskManager
from Task import Task
from datetime import datetime

def main():
    task_manager = TaskManager()

    while True:
        print("\nОберіть опцію:")
        print("1. Створити список завдань")
        print("2. Видалити список завдань")
        print("3. Додати завдання")
        print("4. Видалити завдання")
        print("5. Переглянути завдання")
        print("6. Змінити статус завдання")
        print("7. Змінити завдання")
        print("8. Вийти")

        choice = input("Введіть номер опції: ")

        match choice:
            case '1':
                list_name = input("Введіть ім'я списку: ")
                task_manager.create_list(list_name)

            case '2':
                list_name = input("Введіть ім'я списку для видалення: ")
                task_manager.delete_list(list_name)

            case '3':
                list_name = input("Введіть ім'я списку для додавання завдання: ")
                task_list = task_manager.get_list(list_name)
                if task_list:
                    title = input("Введіть назву завдання: ")
                    description = input("Введіть опис завдання: ")
                    priority = int(input("Введіть пріоритет (1-5): "))
                    end_date = input("Введіть дату завершення завдання (ДД.ММ.РРРР): ")
                    task = Task(title, description, priority, end_date)
                    task_list.add_task(task)
                else:
                    print(f"Список '{list_name}' не знайдено.")

            case '4':
                list_name = input("Введіть ім'я списку для видалення завдання: ")
                task_list = task_manager.get_list(list_name)
                if task_list:
                    task_title = input("Введіть назву завдання для видалення: ")
                    task_list.delete_task(task_title)
                else:
                    print(f"Список '{list_name}' не знайдено.")

            case '5':
                list_name = input("Введіть ім'я списку для перегляду завдань: ")
                task_list = task_manager.get_list(list_name)
                if task_list:
                    sort_option = input("Введіть критерій сортування (date/priority) або натисніть Enter для без сортування: ")
                    task_list.view_tasks(sort_by=sort_option)
                else:
                    print(f"Список '{list_name}' не знайдено.")

            case '6':
                list_name = input("Введіть ім'я списку для зміни статусу завдання: ")
                task_list = task_manager.get_list(list_name)
                if task_list:
                    task_title = input("Введіть назву завдання для зміни статусу: ")
                    task = task_list.get_task_by_title(task_title)
                    if task:
                        task_list.mark_task_as_completed(task)
                    else:
                        print(f"Завдання '{task_title}' не знайдено.")
                else:
                    print(f"Список '{list_name}' не знайдено.")

            case '7':
                list_name = input("Введіть ім'я списку для зміни завдання: ")
                task_list = task_manager.get_list(list_name)
                if task_list:
                    title = input("Введіть назву завдання для зміни: ")
                    new_description = input("Введіть новий опис (або натисніть Enter, щоб залишити старий): ")
                    new_date = input("Введіть нову дату завершення (ДД.ММ.РРРР) або натисніть Enter, щоб залишити стару: ")
                    new_priority = input("Введіть новий пріоритет (1-5) або натисніть Enter, щоб залишити старий: ")

                    task_list.change_task(title, new_description or None, new_date or None, int(new_priority) if new_priority else None)
                else:
                    print(f"Список '{list_name}' не знайдено.")

            case '8':
                print("Вихід з програми...")
                break

            case _:
                print("Невірний вибір! Спробуйте ще раз.")

if __name__ == "__main__":
    main()
