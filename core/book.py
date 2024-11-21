import uuid


class Book:
    def __init__(self, title: str, author: str, year: int, book_id=None, status=True):
        """
        :param title: The title of the book
        :param author: The author of the book
        :param year: The year the book was published
        :param book_id: The unique identifier of the book (optional)
        :param status: Whether the book is available (True) or not (False)
        :type title: str
        :type author: str
        :type year: int
        :type book_id: str or None
        :type status: bool
        """
        if book_id:
            self.book_id = book_id
        else:
            self.book_id = str(uuid.uuid4())
        self.title = title
        self.author = author
        self.year = year
        self.status = status  # True means available

    def __str__(self):
        return F"Название: {self.title} Автор: {self.author} Год издания: ({self.year})"

    def to_dict(self):
        """
        Returns a dictionary representation of the book
        :return: a dictionary with keys 'book_id', 'title', 'author', 'year', 'status'
        :rtype: dict
        """
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }
