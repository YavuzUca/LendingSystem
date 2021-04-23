from Config.file_checker import *
from FrontEnd.Homepage import Page
from Library.Catalog import Catalog
from Library.Book import Book
from Library.Bookitem import Bookitem
from Database.LoanAdministration import LoanAdministration
from Database.UserAdministration import UserAdministration
from Library.Loanitem import Loanitem
from Person.Subscriber import Subscriber


class PublicLibrarySystem:
    def __init__(self):
        file_checker()
        self.catList = []

    def main(self):
        loanAdministration = LoanAdministration()
        UserSystem = UserAdministration()
        horror = Catalog("Horror")
        BookNameOne = Book("Guy", "Corne", "1111111111X", "The Netherlands",
                           "Dutch", "bol.com", "bol.com/777.png", 107, 2001)
        SubOne = Subscriber("Male", "Dutch", "Corne", "den Breejen", "bogerd 9", "2922EA", "Rotterdam",
                           "cornedev@outlook.com", "cornedb", "0180517579")

        horror.addBook(BookNameOne)
        BookCopyItemOne = Bookitem(BookNameOne)
        BookNameOne.update(BookCopyItemOne)
        UserSystem.addSubcriber(SubOne)

        self.setCat(horror)

        LoanOne = Loanitem(SubOne)
        LoanOne.addBookToList(BookCopyItemOne)
        LoanOne.borrowBook()

        loanAdministration.update(LoanOne)

        loanAdministration.createBackup()
        UserSystem.createBackup()
        horror.createBackup()

        loanAdministration.restoreBackup()
        UserSystem.restoreBackup()
        horror.restoreBackup()

        session = Page(self.catList, UserSystem)
        session.homePage()

    def setCat(self, catObj):
        catObj.id = len(self.catList) + 1
        self.catList.append(catObj)


sys = PublicLibrarySystem()
sys.main()

