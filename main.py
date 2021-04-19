from Library.Catalog import Catalog
from Library.Book import Book
from Library.Bookitem import Bookitem
from Database.LoanAdministration import LoanAdministration
from Library.Loanitem import Loanitem
from Person.Subscriber import Subscriber

loanAdministration = LoanAdministration()
horror = Catalog("Horror")
horror.addBookFromFile("booksset1.json")
book = horror.searchBook("Blindness")
print(book.author)