# user_interface.py
from abc import ABC, abstractmethod

class UserInterface(ABC):
    @abstractmethod
    def display_modules(self):
        pass

    @abstractmethod
    def get_module_choice(self):
        pass

    @abstractmethod
    def get_file_path(self):
        pass

    @abstractmethod
    def get_function_choice(self, module_name):
        pass

    @abstractmethod
    def get_line_to_remove(self):
        pass

    @abstractmethod
    def confirm_remove_line(self, line_content):
        pass

    @abstractmethod
    def confirm_save_changes(self):
        pass

    @abstractmethod
    def ask_continue_removal(self):
        pass

    @abstractmethod
    def ask_exit_or_continue(self):
        pass

class ConsoleUserInterface(UserInterface):
    def display_modules(self):
        """Виводить доступні модулі для вибору користувача."""
        print("Оберіть модуль:")
        print("1. Модуль роботи з файлами")
        # Можна додати інші модулі в майбутньому

    def get_module_choice(self):
        """Запитує вибір модуля."""
        return input("Ваш вибір модуля: ")

    def get_file_path(self):
        """Запитує шлях до файлу."""
        return input("Введіть шлях до файлу: ")

    def get_function_choice(self, module_name):
        """Запитує вибір функції в межах модуля."""
        print("Доступні функції:")
        print("1. Читання файлу")
        print("2. Видалити рядок")
        print("3. Зберегти зміни")
        return input("Виберіть функцію: ")

    def get_line_to_remove(self):
        """Запитує у користувача, який рядок він хоче видалити."""
        return int(input("Введіть номер рядка для видалення: ")) - 1

    def confirm_remove_line(self, line_content):
        """Підтверджує видалення рядка."""
        confirm = input(f"Ви хочете видалити рядок: '{line_content}'? (y/n): ").lower()
        return confirm == 'y'

    def confirm_save_changes(self):
        """Підтверджує збереження змін."""
        confirm = input("Ви хочете зберегти зміни? (y/n): ").lower()
        return confirm == 'y'

    def ask_continue_removal(self):
        """Запитує, чи хоче користувач продовжити видаляти наступний рядок."""
        return input("Бажаєте продовжити видаляти рядки? (y/n): ").lower() == 'y'

    def ask_exit_or_continue(self):
        """Запитує, чи хоче користувач вийти з циклу без збереження змін."""
        return input("Вийти без збереження змін? (y/n): ").lower() == 'y'
