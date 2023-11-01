class User:
    def __init__(self, user_id: int, username: str) -> None:
        self.user_id = user_id
        self.username = username
        self.books = []
    
    def info(self):
        return ', '.join(list(sorted(self.books)))

    def __str__(self) -> str:
        return f'{self.user_id}, {self.username}, {self.books}'
