import json

from Library.Book import Book

class Catalog:
    id = 1

    def __init__(self, genre):
        self.list_books = []
        self.id = Catalog.id
        self.genre = genre
        Catalog.id += 1

    def searchBook(self, set_name):
        for i in self.list_books:
            if set_name == i.title:
                return i

    def addBook(self, obj):
        self.list_books.append(obj)

    def addBookFromFile(self, filename):
        try:
            with open(filename, 'r') as file:
                list_json = json.load(file)
                for i in list_json:
                    self.list_books.append(Book(i["title"], i["author"], "000000000X", i["country"], i["language"], i["link"], i["imageLink"], i["pages"], i["year"]))
                print("Forloop task is done")

        except FileNotFoundError:
            return "File not found!"

    def createBackup(self):
        with open('list_booksBackup.json', 'w') as json_file:
            json.dump(self.list_books, json_file)

    def restoreBackup(self):
        try:
            with open('list_booksBackup.json') as json_file:
                self.list_books = json.load(json_file)
        except:
            print("No backup found. Please make one first.")
