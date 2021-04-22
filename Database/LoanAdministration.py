import json
from Library.Book import Book
from Library.Bookitem import Bookitem
from Person.Subscriber import Subscriber

class LoanAdministration:
    def __init__(self):
        self.borrowedBooks = []
    
    def update(self, Loanitem):
        self.borrowedBooks.append(Loanitem)

    def createBackup(self):
        with open('borrowedbooksBackup.json', 'w') as json_file:
            dict_book = []
            for i in self.borrowedBooks:
                list_book = []

                sub_obj = {"id": i.subscriber.id,
                           "gender": i.subscriber.gender,
                           "nameSet": i.subscriber.nameSet,
                           "firstName": i.subscriber.firstName,
                           "surname": i.subscriber.surname,
                           "address": i.subscriber.address,
                           "zipcode": i.subscriber.zipcode,
                           "city": i.subscriber.city,
                           "email": i.subscriber.emailAddress,
                           "username": i.subscriber.username,
                           "telephone": i.subscriber.telephoneNumber,
                            }
                list_book.append(sub_obj)
                for j in i.list_bookitems:
                    arr = {"id": j.id,
                           "title": j.book_obj.title,
                           "author": j.book_obj.author,
                           "ISBN": j.book_obj.ISBN,
                           "country": j.book_obj.country,
                           "language": j.book_obj.language,
                           "link": j.book_obj.link,
                           "image_link": j.book_obj.image_link,
                           "pages": j.book_obj.pages,
                           "year": j.book_obj.year
                           }
                    list_book.append(arr)
                dict_book.append(list_book)
            json.dump(dict_book, json_file)

    def restoreBackup(self):

        with open ('borrowedbooksBackup.json') as json_file:
            json_list = json.load(json_file)
            new_loanitem_list = []
            for i in json_list:
                new_bookitem_list = []
                sub_obj = Subscriber(i["id"], i["gender"], i["nameSet"], i["firstName"], i["surname"], i["address"],
                                     i["zipcode"], i["city"], i["email"], i["username"], i["telephone"])
                new_bookitem_list.append(sub_obj)
                for j in i:
                    obj = Bookitem(j["id"], Book(j["title"], j["author"], "000000000X", j["country"], j["language"],
                                                 j["link"], j["image_link"], j["pages"], j["year"]))
                    new_bookitem_list.append(obj)

                new_loanitem_list.append(new_bookitem_list)

            self.borrowedBooks = new_loanitem_list

