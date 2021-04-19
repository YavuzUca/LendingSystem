class Bookitem:
    id = 1

    def __init__(self, book_obj, available=True):
        self.id = Bookitem.id
        self.book_obj = book_obj
        self.available = available
        Bookitem.id += 1

    def checkAvailability(self):
        if self.available:
            return True
        return False
