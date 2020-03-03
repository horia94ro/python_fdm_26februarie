from oop_project.Person import Person

class Member(Person):




    def __init__(self, name, first_name, age, id):
        super().__init__(name, first_name, age)
        self.id = id
        self.nr_borrowed_books = 0
        self.currently_borrowed_books = []

    def borrow_book(self, book, librarian):
        if librarian.check_available(book):
            self.nr_borrowed_books += 1
            self.currently_borrowed_books.append(book)
            book.borrowed = True
            print("The book was borrowed!")
        else:
            print("The book is not available for borrowing!")


    def return_book(self, book):
        book.borrowed = False
        self.currently_borrowed_books.remove(book)