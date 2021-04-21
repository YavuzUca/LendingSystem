from FrontEnd.Homepage import Page
from Library.Catalog import Catalog
from Library.Book import Book
from Library.Bookitem import Bookitem
from Database.LoanAdministration import LoanAdministration
from Library.Loanitem import Loanitem
from Person.Subscriber import Subscriber
from FrontEnd import Homepage

# loanAdministration = LoanAdministration()
# horror = Catalog("Horror")
# guy = Book("Guy", "Corne", "1111111111X", "The Netherlands", "Dutch", "bol.com", "bol.com/777.png", 107, 2001)
# horror.addBook(guy)
# guyItemOne = Bookitem(guy)
# guyItemTwo = Bookitem(guy)
# guy.update(guyItemOne)
# guy.update(guyItemTwo)
corne = Subscriber(1, "Male", "Dutch", "Corne", "den Breejen", "bogerd 9", "2922EA", "Rotterdam", "cornedev@outlook.com", "cornedb", "0180517579")

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

run = Page()
run.homePage()

