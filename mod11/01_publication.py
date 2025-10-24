class Publication:
    def __init__(self, name: str) -> None:
        self.name = name

    def print_information(self):
        print(self.name)


class Book(Publication):
    def __init__(self, name: str, author: str, page_count: int) -> None:
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        super().print_information()
        print(f"Author: {self.author} Page count: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name: str, chief_editor: str) -> None:
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        super().print_information()
        print(f"Chief Editor: {self.chief_editor}")


pub = Publication("Test Publication")
pub.print_information()

book = Book("Test Book", "Test Author", 150)
book.print_information()

mag = Magazine("Test Magazine", "Test Editor")
mag.print_information()

donald_duck = Magazine("Donald duck", "Aki Hyyppä")
donald_duck.print_information()

compartment = Book("Compartment No. 6", "Rosa Liksom", 192)
compartment.print_information()
