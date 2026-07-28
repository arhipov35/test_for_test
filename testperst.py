from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    year: int
    available: bool = True


class Library:
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def borrow_book(self, title: str):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    raise ValueError(f'"{title}" вже видана.')
                book.available = False
                print(f'📖 Ви взяли "{book.title}"')
                return
        raise ValueError(f'Книгу "{title}" не знайдено.')

    def return_book(self, title: str):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.available = True
                print(f'📚 Ви повернули "{book.title}"')
                return
        raise ValueError(f'Книгу "{title}" не знайдено.')

    def show_books(self):
        print("\n=== Каталог ===")
        for index, book in enumerate(self.books, start=1):
            status = "✅ Доступна" if book.available else "❌ Видана"
            print(
                f"{index}. {book.title} ({book.year}) "
                f"- {book.author} | {status}"
            )


def main():
    library = Library()

    library.add_book(Book("Clean Code", "Robert C. Martin", 2008))
    library.add_book(Book("Fluent Python", "Luciano Ramalho", 2022))
    library.add_book(Book("Python Crash Course", "Eric Matthes", 2023))

    library.show_books()

    print("\nБеремо книгу...\n")
    library.borrow_book("Clean Code")

    library.show_books()

    print("\nПовертаємо книгу...\n")
    library.return_book("Clean Code")

    library.show_books()


if __name__ == "__main__":
    main()