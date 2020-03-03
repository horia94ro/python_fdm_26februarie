from oop_project.Member import Member
from oop_project.Librarian import Librarian
from oop_project.PhysicalBook import PhysicalBook

book1 = PhysicalBook("Harry Potter", "JK Rowling", "Shelf 7", "Home Editure")
john = Member("Sutton", "John", 34, 10)

librarian1 = Librarian("DeSanto", "David", 33, "2020")
john.borrow_book(book1, librarian1)
print(librarian1.check_available(book1))