from core.book import Book
from core.library import Library


def pprint(text: list):
    print("=" * 30)
    for i in text:
        print(i)
        print("=" * 30, end="\n\n")


def create_book():
    print("Добавление книги")
    while True:
        if title := input("Введите название книги: "):
            break
        print("Название не может быть пустым")
    while True:
        if author := input("Введите автора книги: "):
            break
        print("Автор не может быть пустым")
    while True:
        if year := input("Введите год издания книги: "):
            if int(year) > 0:
                break
        print("Год издания не может быть пустым, и должен быть больше 0")
    return Book(title, author, year)


def delete_book(library: Library):
    book_id = input("ВВедите id книги: ")
    try:
        res = library.remove_book(book_id)
        if res["status"]:
            pprint(["Книга удалена!"])
        else:
            pprint([res["message"]])
    except ValueError as e:
        print(e)


def search_book(library: Library):
    print("Поиск книги.")
    title = input(
        "Введите название книги. Или ничего для поиска по автору или году: ")
    if len(title) == 0:
        title = None
    author = input(
        "Введите автора книги. Или ничего для поиска по названию или году: ")
    if len(author) == 0:
        author = None
    year = input(
        "Введите год издания книги. Или ничего для поиска по названию или автору: "
    )
    if len(year) == 0:
        year = None
    res = library.find_book(title=title, author=author, year=year)
    if res["status"]:
        print("Найденные книги: ")
        pprint(res["books"])
    else:
        pprint(res["message"])


def show_all_books(library: Library):
    res = library.show_all_books()
    if res["status"]:
        resp = [
            F"ID: {book_id}\n{book}\nСтатус: {'В наличии' if book.status else 'Выдана'}"
            for book_id, book in res["books"].items()
        ]
        pprint(resp)
    else:
        pprint(res["message"])


def change_status(library: Library):
    book_id = input("ВВедите id книги: ")
    status = input("ВВедите новый статус (1 - в наличии, 0 - выдана): ")
    try:
        res = library.change_status(book_id, bool(int(status)))
        if res["status"]:
            pprint(["Статус изменен!"])
        else:
            pprint([res["message"]])
    except ValueError as e:
        print("Ошибка при изменении статуса: ", e)


def main():
    library = Library("Главная")
    while True:
        print("Выберите действие:", end="\n\n")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменение статуса книги")
        print("6. Выход")
        print()
        choice = input("Введите номер действия: ")
        if choice == "1":
            book = create_book()
            library.add_book(book)
        elif choice == "2":
            delete_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            show_all_books(library)
        elif choice == "5":
            change_status(library)
        elif choice == "6":
            break
