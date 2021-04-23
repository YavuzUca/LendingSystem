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
                return self.user_page()
        print("That name does not exist. You should register first.\n")
        return self.homePage()

    def searchBook(self):
        try:
            user_input = input()
            for cat in self.list_cat:
                search = cat.searchBook(user_input)
                if user_input == search.title:
                    print(f"Title: {cat.searchBook(user_input).title}\nCopies left: {len(cat.searchBook(user_input).list_book)}\n")
                    return self.user_page() if self.currently_loggedin is not None else self.homePage()
        except AttributeError:
            print("Book does not exist.\n")
            return self.user_page() if self.currently_loggedin is not None else self.homePage()

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
