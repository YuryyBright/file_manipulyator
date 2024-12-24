# main_program.py
from file_operations import TextFileOperations
from user_interface import ConsoleUserInterface


class MainProgram:
    def __init__(self, file_operations, user_interface):
        self.file_operations = file_operations
        self.user_interface = user_interface

    def run(self):
        while True:
            self.user_interface.display_modules()
            module_choice = self.user_interface.get_module_choice()

            if module_choice == '1':  # Модуль роботи з файлами
                # Користувач обирає файл
                file_path = self.user_interface.get_file_path()

                # Запитуємо, яку операцію виконати
                while True:
                    function_choice = self.user_interface.get_function_choice("FileOperations")

                    if function_choice == '1':  # Читання файлу
                        line_number = int(input("Введіть номер рядка для перегляду: ")) - 1
                        line_content = self.file_operations.read_lines(file_path)
                        if line_content is not None:
                            print(f"Рядок {line_number + 1}: {line_content}")
                        else:
                            print("Рядок не знайдений!")

                    elif function_choice == '2':  # Видалення рядка
                        # Читаємо всі рядки файлу
                        lines = self.file_operations.read_lines(file_path)

                        if not lines:
                            print("Файл порожній або не знайдений.")
                            continue

                        # Цикл для поетапного видалення рядків
                        while True:
                            for i, line in enumerate(lines):
                                print(f"{i + 1}. {line.strip()}")
                                action = input(
                                    "Виберіть опцію: \n1. Видалити рядок\n2. Пропустити рядок\n3. Вийти без змін\n4. Зберегти зміни та вийти\n")

                                if action == '1':  # Видалити рядок
                                    if self.user_interface.confirm_remove_line(line.strip()):
                                        self.file_operations.remove_line(file_path, i)
                                        print("Рядок видалено!")
                                elif action == '2':  # Пропустити рядок
                                    continue
                                elif action == '3':  # Вийти без змін
                                    if self.user_interface.ask_exit_or_continue():
                                        print("Зміни не збережені. Вихід.")
                                        break
                                elif action == '4':  # Зберегти зміни
                                    self.file_operations.write_to_file(file_path, lines)
                                    print("Зміни збережено!")
                                    break
                                else:
                                    print("Невірний вибір. Повторіть.")
                            if action in ('3', '4'):  # Якщо користувач вийшов або зберіг зміни, завершуємо цикл
                                break

                    elif function_choice == '3':  # Зберегти зміни
                        if self.user_interface.confirm_save_changes():
                            lines = self.file_operations.read_lines(file_path)
                            self.file_operations.write_to_file(file_path, lines)
                            print("Зміни збережено!")
                        else:
                            print("Збереження скасовано.")
                        break  # Перериваємо цикл функцій

                    else:
                        print("Невірний вибір функції.")

            else:
                print("Невірний вибір модуля. Спробуйте ще раз.")

            # Запит користувача на продовження
            continue_choice = input("\nБажаєте виконати іншу операцію? (y/n): ").lower()
            if continue_choice != 'y':
                break


if __name__ == "__main__":
    file_operations = TextFileOperations()
    user_interface = ConsoleUserInterface()

    program = MainProgram(file_operations, user_interface)
    program.run()
