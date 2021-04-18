from Person.Person import Person

class Librarian(Person):
    def __init__(self, id, gender, firstName, surname, nameSet, username, password):
        super().__init__(id, gender, nameSet, firstName, surname, 2)
        self.username = username
        self.password = password

    def getObject(self):
        return self