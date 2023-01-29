BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:
    def __init__(self, id_, name, pages):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга {self.name!r}'

    def __repr__(self) -> str:
        return f"Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})"

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        f"Book(id_={self.id}, name={self.name}, pages={self.pages})" for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
