from Database.LoanAdministration import LoanAdministration
from Database.UserAdministration import UserAdministration
from Library.Loanitem import Loanitem
from Person.Subscriber import Subscriber
from Person.Librarian import Librarian
from Library.Book import Book
from Library.Bookitem import Bookitem
from Library.Catalog import Catalog


class Page:
    def __init__(self):
        self.currently_loggedin = None
        self.currently_loggedin_perm = None
        self.usersystem = UserAdministration()
        self.loansystem = LoanAdministration()
        self.listsAllCat = []
        self.Default()

    def Default(self):

        horror = Catalog("Horror")
        BookNameOne = Book("Corne", "The Netherlands",
                           "Dutch", "bol.com", "bol.com/777.png", 107, "Guy", 2001)
        SubOne = Subscriber("Male", "Dutch", "Corne", "den Breejen", "bogerd 9", "2922EA", "Rotterdam",
                            "cornedev@outlook.com", "cornedb", "0180517579")
        SubTwo = Librarian("Male", "Vuuzie", "Dutch", "Uca", "Vuuzie", "2922EA")

        drama = Catalog("Drama")
        BookNameTwo = Book("Corne", "The Netherlands",
                           "Dutch", "bol.com", "bol.com/777.png", 107, "Lifeliner", 2001)
        drama.addBook(BookNameTwo)
        BookCopyItemTwo = Bookitem(BookNameTwo)
        BookCopyItemTwoOne = Bookitem(BookNameTwo)
        BookNameTwo.update(BookCopyItemTwo)
        BookNameTwo.update(BookCopyItemTwoOne)

        horror.addBook(BookNameOne)
        BookCopyItemOne = Bookitem(BookNameOne)
        BookNameOne.update(BookCopyItemOne)
        self.usersystem.addSubcriber(SubOne)
        self.usersystem.addLibrarian(SubTwo)
        self.listsAllCat.append(horror)
        self.listsAllCat.append(drama)
        #
        #
        # LoanOne = Loanitem(SubOne)
        # LoanOne.addBookToList(BookCopyItemOne)
        # LoanOne.borrowBook()
        #
        # loanAdministration.update(LoanOne)
        # drama.createBackup()
        # loanAdministration.createBackup()
        # UserSystem.createBackup()
        # horror.createBackup()
        #
        # loanAdministration.restoreBackup()
        # UserSystem.restoreBackup()
        # horror.restoreBackup()

    def homePage(self):
        print()
        print("1. Login")
        print("2. Search Book")
        print("3. Register subscriber")
        print("4. Quit\n")

        keypress = input()
        if keypress == "1":
            self.logIn()
        elif keypress == "2":
            self.searchBook()
        elif keypress == "3":
            self.registerUser()
        elif keypress == "4":
            try:
                quit()
            except:
                quit()
        else:
            print("Invalid keypress\n")
            self.homePage()

    def registerUser(self):
        gender_input = input("Enter your gender (Male/Female: ")
        name_set_input = input("Enter your nationalty: ")
        username_input = input("Enter your username: ")
        while (not self.username_check(username_input)):
            username_input = input("Enter your username: ")
        firstName_input = input("Enter your first name: ")
        surname_input = input("Enter your surname: ")
        address_input = input("Enter your home address (street name + housenumber): ")
        zipcode_input = input("Enter your zipcode (Format: 0000AA): ")
        city_input = input("Enter your city: ")
        emailAddress_input = input("Enter your emailaddress: ")
        phonenumber_input = str(input("Enter your phone number: "))

        newSubscriber = Subscriber(gender_input, name_set_input, firstName_input, surname_input, address_input,
                                   zipcode_input, city_input, emailAddress_input, username_input, phonenumber_input)
        self.usersystem.addSubcriber(newSubscriber)

        print("User " + username_input + " has been created")
        return self.homePage()

    def username_check(self, username_input):
        for user in self.usersystem.personlist:
            if username_input == user.username:
                print("Usernamer already in use, please type another.")
                return False
        return True

    def logIn(self):
        print("Please enter your username:")
        user_input = input()
        for i in self.usersystem.personlist:
            if i.username == user_input:
                self.currently_loggedin = i.username
                self.currently_loggedin_perm = i.permissionLevel
                if i.permissionLevel == 0:
                    return self.admin_page()
                else:
                    return self.user_page()
        print("That name does not exist. You should register first.\n")
        return self.homePage()

    def searchBook(self):
        print("You can search for a book here on multiple fields, the fields may be left empty.\n")
        title = input("What's the title of the book: ")
        author = input("Who's the author of the book: ")
        country = input("In what country does the book come from: ")
        language = input("What's the language of the book: ")
        pages = input("How many pages does the book have: ")
        if pages.strip() != "":
            pages = int(pages)
        else:
            pages = 0
        year = input("In what year is the book published: ")
        if year.strip() != "":
            year = int(year)
        else:
            year = 0

        books = []
        for cat in self.listsAllCat:
            tmpBooks = cat.searchBook(title, author, country, language, pages, year)
            if tmpBooks:
                books.append(tmpBooks)

        if not books:
            print("\nCould not find a book by the given criteria.\n")
            return self.homePage() if self.currently_loggedin is None else self.user_page() if self.currently_loggedin_perm == 1 else self.admin_page()

        for catalog in books:
            for book in catalog:
                print("\nTitle: " + book.title)
                print("Author: " + book.author)
                print("Country: " + book.country)
                print("Amount of pages: " + str(book.pages))
                if book.checkAvailibility():
                    print("In stock: Yes" + "\n")
                else:
                    print("In stock: No" + "\n")
        return self.homePage() if self.currently_loggedin is None else self.user_page() if self.currently_loggedin_perm == 1 else self.admin_page()

    def user_page(self):
        print("1. Search Book")
        print("2. My Rented Books")
        print("3. My Usersettings")
        print("4. Rent book")
        print("5. Hand in book")
        print("6. Log out\n")

        keypress = input()
        if keypress == "1":
            self.searchBook()
        elif keypress == "2":
            self.myloans()
        elif keypress == "3":
            self.myinfo()
        elif keypress == "4":
            self.rent_book()
        elif keypress == "5":
            self.hand_book()
        elif keypress == "6":
            self.currently_loggedin = None
            self.currently_loggedin_perm = None
            self.homePage()
        else:
            print("Invalid keypress")
            self.user_page()

    def myinfo(self):
        for i in self.usersystem.personlist:
            if self.currently_loggedin == i.username:
                print("Your id              = " + i.id)
                print("Your gender          = " + i.gender)
                print("Your nationality     = " + i.nameSet)
                print("Your first name      = " + i.firstName)
                print("Your surname         = " + i.surname)
                print("Your address         = " + i.address)
                print("Your zipcode         = " + i.zipcode)
                print("Your city            = " + i.city)
                print("Your emailaddress    = " + i.emailAddress)
                print("Your phone number    = " + i.telephoneNumber)

        return self.user_page()

    def myloans(self):
        for loanitem in self.loansystem.borrowedBooks:
            if self.currently_loggedin == loanitem.subscriber.username:
                for book_item in loanitem.list_bookitems:
                    print(
                        f"Name: {book_item.book_obj.title}\nStartdate: {loanitem.startdate}\nEnddate: {loanitem.enddate}\n")

        return self.user_page()

    def rent_book(self):
        sub = self.get_subobject()
        loan = Loanitem(sub)
        search_input = input("Add a book to your list by typing it's title: ")
        for cat in self.listsAllCat:
            for book in cat.list_books:
                if search_input == book.title:
                    if not book.checkAvailibility():
                        print("Book is out of stock.")
                        return self.user_page()
                    for copy in book.list_book:
                        if copy.checkAvailability():
                            loan.addBookToSingleList(copy)
                            print("Book added.")
                            loan.borrowBook()
                            self.loansystem.update(loan)
                            return self.user_page()
        print("Error, book not found.")
        return self.user_page()

    def get_subobject(self):
        for sub in self.usersystem.personlist:
            if self.currently_loggedin == sub.username:
                return sub

    def admin_page(self):
        print("1. Create Category")
        print("2. Search Book")
        print("3. Add Book")
        print("4. Delete Book")
        print("5. Add Copy")
        print("6. Backup")
        print("7. Log out\n")

        keypress = input()
        if keypress == "1":
            self.createCategory()
        elif keypress == "2":
            self.searchBook()
        elif keypress == "3":
            self.createBook()
        elif keypress == "4":
            self.deleteBook()
        elif keypress == "5":
            self.addCopy()
        elif keypress == "6":
            self.makeBackup()
        elif keypress == "7":
            self.currently_loggedin = None
            self.currently_loggedin_perm = None
            self.homePage()
        else:
            print("Invalid keypress\n")
            self.admin_page()

    def createCategory(self):
        print("Enter the name of the Catalog you want to add.\n")
        name = input()
        if type(name) is not str:
            print("Error, the name is not valid. Do you still want to continue? y/n")
            answer = input()
            if answer == "y":
                return self.createCategory()
            else:
                return self.admin_page()

        print("Catalog added.")
        catalog = Catalog(name)
        catalog.id = len(self.listsAllCat) + 1
        self.listsAllCat.append(catalog)

        return self.admin_page()

    def createBook(self):
        print("Please type the name of the author, country, link of an image, "
              "language, link, the amount of pages, title and year in this order.")
        print("IMPORTANT: Make sure that the pages and year are numbers, not words/letters.")
        author = input()
        country = input()
        imageLink = input()
        language = input()
        link = input()
        pages = int(input())
        title = input()
        year = int(input())
        if type(author) is str and type(country) is str and type(imageLink) is str and type(language) is str and type(
                link) is str and type(pages) is int and type(title) is str and type(year) is int:
            print("Add book to a specific catalog? y/n\n")
            ans = input()
            if ans == "y":
                print("Type name of the Category.\n")
                namecat = input()
                while not namecat in [i.genre for i in self.listsAllCat]:
                    print("Name category does not exist, try again.\n")
                    namecat = input()
                for i in self.listsAllCat:
                    if i.genre == namecat:
                        book = Book(author, country, imageLink, language, link, pages, title, year)
                        i.addBook(book)
                        print("Book has been added.")
                        return self.admin_page()
            else:
                for i in self.listsAllCat:
                    if i.genre == "No_Category":
                        book = Book(author, country, imageLink, language, link, pages, title, year)
                        i.addBook(book)
                        return self.admin_page()

                catalog = Catalog("No_Category")
                catalog.id = len(self.listsAllCat) + 1
                book = Book(author, country, imageLink, language, link, pages, title, year)
                catalog.addBook(book)

                self.listsAllCat.append(catalog)
                return self.admin_page()

    def deleteBook(self):
        print("Type the name of the book you want to delete.\n")
        bookname = input()
        for cat in self.listsAllCat:
            for book in cat.list_books:
                if book.title == bookname:
                    print(f"Book {book.title} found")
                    for bookcopy in book.list_book:
                        if not bookcopy.checkAvailability():
                            print("You cannot delete a book when somebody has a copy of the book.\n")
                            return self.admin_page()
                    print("Book has been deleted.")
                    cat.list_books.remove(book)
                    return self.admin_page()
            print("Could not find a book with that title.\n")
            return self.admin_page()

    def makeBackup(self):
        for i in self.listsAllCat:
            i.createBackup()
        self.usersystem.createBackup()
        self.loansystem.createBackup()
        print("Backups has been made of the system.")
        return self.admin_page()

    def addCopy(self):
        name = input("What is the title of the book you want to add a copy of?\n")
        for cat in self.listsAllCat:
            for book in cat.list_books:
                if book.title == name:
                    print(book)
                    bookitem = Bookitem(book)
                    book.update(bookitem)
                    print("Book copy added!")
                    return self.admin_page()

        print("It appears that the booktitle you put does not exist.")
        return self.admin_page()

    def hand_book(self):
        for loanitem in self.loansystem.borrowedBooks:
            if self.currently_loggedin == loanitem.subscriber.username:
                for book_item in loanitem.list_bookitems:
                    print(
                        f"Name: {book_item.book_obj.title}\nStartdate: {loanitem.startdate}\nEnddate: {loanitem.enddate}\n")
        print("These are your rented books. If there is nothing, that means that you have nothing rented.")
        book = input("Type in the title of the book you want to return.\n")
        count = 0
        for loanitem in self.loansystem.borrowedBooks:
            if self.currently_loggedin == loanitem.subscriber.username:
                for book_item in loanitem.list_bookitems:
                    if book_item.book_obj.title == book:
                        book_item.returnBookitem()
                        loanitem.list_bookitems.remove(book_item)
                        count += 1
        if count < 1:
            print("Book has not been found, wrong name?")
            return self.user_page()
        else:
            print("Book returned")
            return self.user_page()
