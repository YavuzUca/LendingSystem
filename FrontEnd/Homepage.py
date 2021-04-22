class Page:
    def __init__(self, category, usersys):
        self.currently_loggedin = None
        self.category = category
        self.usersystem = usersys

    def homePage(self):
        print("1. Inloggen")
        print("2. Search Book")
        print("3. Quit\n")

        keypress = input()
        if keypress == "1":
            self.logIn()
        elif keypress == "2":
            user_input = input()
            for book in self.category.list_books:
                for bookitems in book.list_book:
                    if user_input == book.title:
                        print(f"{bookitems.id} - {book.title}")

        elif keypress == "3":
            quit()
        else:
            print("Invalid keypress")
            self.homePage()

    def logIn(self):
        user_input = input()
        for i in self.usersystem:
            if i.firstName == user_input:
                self.currently_loggedin = i.firstName

    def user_page(self):
        print("1. Search Book")
        print("2. My Rented Books")
        print("3. My Usersettings")
        print("4. Log out\n")

        keypress = input()
        if keypress == "1":
            pass
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
