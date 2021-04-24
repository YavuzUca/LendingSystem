class Page:
    def __init__(self, category, usersys):
        self.currently_loggedin = None
        self.list_cat = category
        self.usersystem = usersys

    def homePage(self):
        print("1. Login")
        print("2. Search Book")
        print("3. Quit\n")

        keypress = input()
        if keypress == "1":
            self.logIn()
        elif keypress == "2":
            self.searchBook()
        elif keypress == "3":
            try:
                quit()
            except:
                quit()
        else:
            print("Invalid keypress\n")
            self.homePage()

    def logIn(self):
        print("Please enter your firstname:")
        user_input = input()
        for i in self.usersystem.personlist:
            if i.firstName == user_input:
                self.currently_loggedin = i.firstName
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
        for cat in self.list_cat:
            tmpBooks = cat.searchBook(title, author, country, language, pages, year)
            if tmpBooks:
                books.append(tmpBooks)

        if not books:
            print("\nCould not find a book by the given criteria.\n")
            return self.homePage() if self.currently_loggedin is None else self.user_page()

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
                


    def user_page(self):
        print("1. Search Book")
        print("2. My Rented Books")
        print("3. My Usersettings")
        print("4. Log out\n")

        keypress = input()
        if keypress == "1":
            self.searchBook()
        elif keypress == "2":
            pass
        elif keypress == "3":
            pass
        elif keypress == "4":
            self.currently_loggedin = None
            self.homePage()
        else:
            print("Invalid keypress")
            self.user_page()

    def admin_page(self):
        print("1. Search Book")
        print("2. Add Book")
        print("4. Log out\n")
