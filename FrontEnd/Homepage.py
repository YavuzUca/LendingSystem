


class Page:
    def homePage(self):
        print("1. Inloggen")
        print("2. Search Book")
        print("3. Quit\n")

        keypress = input()
        if keypress == "1":
            self.logIn()
        elif keypress == "2":
            pass
        elif keypress == "3":
            quit()
        else:
            print("Invalid keypress")
            self.homePage()

    def logIn(self):
        keypress = input()
