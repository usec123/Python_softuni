from .user import User

class Library:
    def __init__(self) -> None:
        self.user_records = [] # User
        self.books_available = dict() # author - str : books - str list
        self.rented_books = dict() # usernames - str : dict => book name - str : days left - int
    
    def get_book(self, author:str, book_name:str, days_to_return:int, user: User):
        if book_name in self.books_available.values():
            user.books.append(book_name)
            if user.username not in self.rented_books:
                self.rented_books[user.username] = dict()
            self.rented_books[user.username][book_name] = days_to_return
            self.books_available[author].remove(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        days_left = None
        for d in self.rented_books.values():
            if book_name in d:
                days_left = d[book_name]
                break
        return f'The book "{book_name}" is already rented and will be available in {days_left} days!'
        
    def return_book(self, author:str, book_name:str, user: User):
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            self.rented_books[user.username].pop(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"
