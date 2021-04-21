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
                    self.list_books.append(
                        Book(i["title"], i["author"], "000000000X", i["country"], i["language"], i["link"],
                             i["image_link"], i["pages"], i["year"]))
                print("Forloop task is done")

        except FileNotFoundError:
            return "File not found!"

    def createBackup(self):
        with open('list_booksBackup.json', 'w') as json_file:
            dict_book = []
            for i in self.list_books:
                list_b = []
                for j in i.list_book:
                    arr = {"id": j.id,
                           "available": j.available}
                    list_b.append(arr)
                arr = {"title": i.title,
                       "author": i.author,
                       "ISBN": i.ISBN,
                       "country": i.country,
                       "language": i.language,
                       "link": i.link,
                       "image_link": i.image_link,
                       "pages": i.pages,
                       "year": i.year,
                       "list_book": list_b,
                       }
                dict_book.append(arr)
            json.dump(dict_book, json_file)

    def restoreBackup(self):
        try:
            with open('list_booksBackup.json') as json_file:
                json_list = json.load(json_file)
                new_list = []
                for i in json_list:
                    obj = Book(i["title"], i["author"], "000000000X", i["country"], i["language"], i["link"],
                               i["image_link"], i["pages"], i["year"])
                    obj.list_book.append([j for j in i["list_book"]])
                    new_list.append(obj)

                self.list_books = new_list
        except:
            print("No backup found. Please make one first.")
