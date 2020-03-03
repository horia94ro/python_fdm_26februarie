from oop_project.Book import Book

class PhysicalBook(Book):




    def __init__(self, title, author, location, publishing_house):
        super().__init__(title, author)
        self.location = location
        self.publishing_house = publishing_house
        self.borrowed = False