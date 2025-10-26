import json
from pathlib import Path

class Library:
    def __init__(self):
        self.books_path = Path(__file__).parent.parent.parent / "database" / "bookInfo.json"
        self.books = self.__load_data(self.books_path)

    def __load_data(self, path):
        if path.exists():
            with open(path, "r") as f:
                return json.load(f)
        return {}

    def __save_data(self, path, data):
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

    def add_book(self, title, author, quantity):
        self.books[title] = {"author": author, "quantity": quantity}
        self.__save_data(self.books_path, self.books)

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            self.__save_data(self.books_path, self.books)

    def show_books(self):
        books: dict = self.books
        for book in books:
            if book["quantity"] > 0:
                print(book["title"])
