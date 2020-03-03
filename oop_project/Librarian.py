from oop_project.Person import Person

class Librarian(Person):





    def __init__(self, name, first_name, age, hire_date):
        super().__init__(name, first_name, age)
        self.hire_date = hire_date

    def check_available(self, book):
        if book.borrowed:
            print("The book is not available!")
            return False
        else:
            print("The book is available!")
            return True