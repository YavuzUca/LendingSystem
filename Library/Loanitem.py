import datetime


class Loanitem:
    id = 1

    def __init__(self, sub_obj):
        self.id = Loanitem.id
        self.list_bookitems = []
        self.subscriber = sub_obj
        self.startdate = datetime.date.today()
        self.enddate = self.enddate()
        Loanitem.id += 1

    def enddate(self):
        date = datetime.date.today()
        day = date.day
        month = date.month + 1
        year = date.year
        if month == 12:
            year += 1
            month += 1
        return datetime.date(year, month, day)

    def addBookToList(self, obj):
        if obj.checkAvailability():
            self.list_bookitems.append(obj)
            obj.available = False
        else:
            print("Book not available")

    def borrowBook(self):
        for i in self.list_bookitems:
            i.available = False
