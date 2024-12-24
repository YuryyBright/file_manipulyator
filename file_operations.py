# file_operations.py
from abc import ABC, abstractmethod
import os


class FileOperations(ABC):
    @abstractmethod
    def read_lines(self, file_path, num_lines=None):
        """Читання рядків з файлу. Якщо num_lines задано, зчитуємо тільки цю кількість рядків."""
        pass

    @abstractmethod
    def write_to_file(self, file_path, lines):
        """Запис змін у файл."""
        pass

    @abstractmethod
    def remove_line(self, file_path):
        """Видалення рядка з файлу построчно."""
        pass


class TextFileOperations(FileOperations):
    def read_lines(self, file_path, num_lines=None):
        """Читає кілька рядків з файлу. Якщо num_lines не задано, читаємо всі рядки."""
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                if num_lines:
                    return lines[:num_lines]  # Повертає лише задану кількість рядків
                return lines  # Якщо num_lines не вказано, повертаємо всі рядки
        except FileNotFoundError:
            print("Файл не знайдено.")
            return []

    def write_to_file(self, file_path, lines):
        """Записує список рядків назад у файл."""
        try:
            with open(file_path, 'w') as file:
                file.writelines(lines)
        except Exception as e:
            print(f"Помилка при записі у файл: {e}")

    def remove_line(self, file_path):
        """Видаляти рядки з файлу построчно."""
        try:
            temp_file_path = f"{file_path}.temp"
            lines_to_keep = []

            with open(file_path, 'r') as read_file, open(temp_file_path, 'w') as write_file:
                line_number = 0
                while True:
                    line = read_file.readline()
                    if not line:  # Кінець файлу
                        break

                    print(f"Рядок {line_number + 1}: {line.strip()}")
                    action = input(
                        "Виберіть опцію: \n1. Видалити рядок\n2. Пропустити рядок\n3. Вийти без змін\n4. Зберегти зміни та вийти\n")

                    if action == '1':  # Видалити рядок
                        # Запитуємо користувача, чи він точно хоче видалити
                        confirm = input(f"Ви хочете видалити цей рядок: {line.strip()}? (y/n): ").lower()
                        if confirm == 'y':
                            continue  # Не записуємо рядок
                    elif action == '2':  # Пропустити рядок
                        write_file.write(line)  # Записуємо рядок
                        lines_to_keep.append(line)  # Зберігаємо цей рядок для відновлення
                    elif action == '3':  # Вийти без змін
                        if input("Вийти без збереження змін? (y/n): ").lower() == 'y':
                            break
                    elif action == '4':  # Зберегти зміни
                        print("Зміни збережено!")
                        break

                    line_number += 1

            # Після того, як зміни зроблені, замінюємо оригінальний файл на новий
            os.replace(temp_file_path, file_path)
            print(f"Зміни збережено в файлі {file_path}")

        except FileNotFoundError:
            print("Файл не знайдено.")
        except Exception as e:
            print(f"Помилка при видаленні рядка: {e}")

#A:\VK Parsing 2023 (0).txt