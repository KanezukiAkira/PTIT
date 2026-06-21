class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity

    def __str__(self):
        return f"{self.book_id} | {self.title} | {self.author} | {self.quantity}"