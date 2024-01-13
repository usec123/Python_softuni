from typing import List, Optional


class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def find_book(self, title) -> Optional[Book]:
        try:
            return [book for book in self.books if book.title.lower() == title.lower()  ][0]
        except IndexError:
            return None
