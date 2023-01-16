from task1 import Book, BOOKS_DATABASE

class Library:
    def __init__(self, books = None):
        self.books = books

    def get_next_book_id(self):
    """ возвращает идентификатор для добавления новой книги в библиотеку """
        if self.books:
            return self.books[-1].id_
        else:
            return 1

    def get_index_by_book_id(self, id_):
    """ возвращает индекс книги в списке """
        for index, book in enumerate(self.books):
            if book.id_ == id_:
                return self.books.index(book)
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
