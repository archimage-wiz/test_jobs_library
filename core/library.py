import json
from core.book import Book
from config import LIBRARY_DATA


class Library:
    def __init__(self, name: str):
        """Initialize Library object.
        Args:
            name (str): Name of the library
        """
        self.name = name
        self.__books = self.__read_library()

    def __str__(self):
        return F"Добро пожаловать в библиотеку{self.name}"

    def __save_library(self):
        try:
            with open(LIBRARY_DATA, 'w', encoding="utf-8") as f:
                json.dump({str(k): v.to_dict() for k, v in self.__books.items()}, f)
        except IOError as e:
            print(f"Ошибка при сохранении библиотеки: {e}")

    def __read_library(self) -> dict:
        try:
            with open(LIBRARY_DATA, 'r', encoding="utf-8") as f:
                res = json.load(f)
                for k, v in res.items():
                    res[k] = Book(**v)
                return res
        except FileNotFoundError:
            print("Файл библиотеки не найден. Создана пустая библиотека.")
            return {}

    def add_book(self, book: Book) -> dict:
        """Add book to library
        Args:
            book (Book): Book object
        Returns:
            dict: Status of operation
        """
        if book.book_id in self.__books:
            return {"status": False, "message": "Книга уже существует"}
        self.__books[book.book_id] = book
        self.__save_library()
        return {"status": True, "message": "Книга добавлена"}

    def remove_book(self, book_id: str) -> dict:
        """Remove a book from the library.
        Args:
            book_id (str): The unique identifier of the book to be removed.
        Returns:
            dict: A dictionary containing the status of the operation and a message.
                If successful, returns {"status": True, "message": "Книга удалена"}.
                If the book is not found, returns {"status": False, "message": "Книга не найдена"}.
        """
        if book_id not in self.__books:
            return {"status": False, "message": "Книга не найдена"}
        del self.__books[book_id]
        self.__save_library()
        return {"status": True, "message": "Книга удалена"}

    def find_book(self, title=None, author=None, year=None) -> list:
        """Search for a book in the library.
        Args:
            title (str): The title of the book to search for.
            author (str): The author of the book to search for.
            year (int): The year the book was published.
        Returns:
            A dictionary containing the status of the search and a message.
            If the search was successful, the dictionary will contain a list of books
            that match the search criteria.
        """
        if not any([title, author, year]):
            return {"status": False, "message": "Нет параметров для поиска"}
        results = []
        for book in self.__books.values():
            if title:
                key_words = title.lower().split(" ")
                for word in key_words:
                    if word in book.title.lower():
                        results.append(book)
                        break
            if author:
                if author.lower() == book.author.lower():
                    results.append(book)
            if year:
                if year == book.year:
                    results.append(book)
        results = list(set(results))
        if not results:
            return {"status": False, "message": "Книга не найдена"}
        return {"status": True, "message": "Книга найдена", "books": results}

    def show_all_books(self) -> dict:
        """Returns all books in the library.
        Returns:
            A dictionary containing the status of the request and a message.
            If the library is empty, the dictionary will contain a message indicating that.
            If the library is not empty, the dictionary will contain a list of all books in the library.
        """
        if not self.__books:
            return {"status": False, "message": "Библиотека пуста"}
        return {"status": True, "message": "Все книги", "books": self.__books.copy()}

    def change_status(self, book_id: str, status: bool) -> dict:
        """Changes the status of a book in the library.
        Args:
            book_id (str): The unique identifier of the book to change the status of.
            status (bool): The new status of the book.
        Returns:
            A dictionary containing the status of the operation and a message.
            If the book is not found, returns {"status": False, "message": "Книга не найдена"}.
            If the operation is successful, returns {"status": True, "message": "Статус изменен"}.
        """
        if book_id not in self.__books.keys():
            return {"status": False, "message": "Книга не найдена"}
        self.__books[book_id].status = status
        self.__save_library()
        return {"status": True, "message": "Статус изменен"}
