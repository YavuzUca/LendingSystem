from FrontEnd.Homepage import Page
from Library.Catalog import Catalog
from Library.Book import Book
from Library.Bookitem import Bookitem
from Database.LoanAdministration import LoanAdministration
from Database.UserAdministration import UserAdministration
from Library.Loanitem import Loanitem
from Person.Subscriber import Subscriber


loanAdministration = LoanAdministration()
horror = Catalog("Horror")
guy = Book("Guy", "Corne", "1111111111X", "The Netherlands", "Dutch", "bol.com", "bol.com/777.png", 107, 2001)

guy_copy = Bookitem(guy)
horror.addBook(guy)
guyItemOne = Bookitem(guy)
guy.update(guyItemOne)
corne = Subscriber("Male", "Dutch", "Corne", "den Breejen", "bogerd 9", "2922EA", "Rotterdam", "cornedev@outlook.com", "cornedb", "0180517579")
UserSystem = UserAdministration()
UserSystem.addCustomer(corne)
session = Page(horror, UserSystem)
session.homePage()


# loanList = Loanitem(corne)
# loanList.addBookToList(guyItemOne)
# loanAdministration.update(loanList)
# horror.createBackup()
# horror.addBookFromFile("list_booksBackup.json")
# print([i.title for i in horror.list_books])
# loanAdministration.createBackup()
# horror.restoreBackup()
# for i in horror.list_books:
#     print(i.title)
#     for j in i.list_book:
#         print(j)

# run = Page()
# run.homePage()
# system = LoanAdministration()
# loanitem = Loanitem(corne)
# loanitem.addBookToList(guy_copy)

# system.update(loanitem)
# system.createBackup()
# print(system.borrowedBooks)
# system2 = LoanAdministration()
# system2.restoreBackup()
# print(system2.borrowedBooks)
# print(guy_copy.available)
# for i in system.borrowedBooks:
#     print(i.id)
#     print(i.list_bookitems[0].book_obj.title)
