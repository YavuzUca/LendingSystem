import csv
import json, random

from Person.Subscriber import Subscriber
from Person.Librarian import Librarian

class UserAdministration:
    personlist = []

    def addCustomersFromCsvFile(self, File):
        with open(File, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.addSubcriber(Subscriber(0 ,row['Gender'], row['NameSet'], row['GivenName'], row['Surname'], row['StreetAddress'], row['ZipCode'], row['City'], row['EmailAddress'], row['Username'], row['TelephoneNumber']))
                
            return self.personlist
    
    def addCustomersFromJsonFile(self, File):
        with open(File, 'r') as json_file:
            json_list = json.load(json_file)
            for row in json_list:
                if row['permissionlevel'] == 1:
                    self.addSubcriber(Subscriber(row["Gender"], row["Nameset"], row["GivenName"], row["Surname"], row["StreetAddress"],
                                row["ZipCode"], row["City"], row["EmailAddress"], row["Username"], row["TelephoneNumber"], row["permissionlevel"]))
                else:
                    self.addLibrarian(Librarian(row["Gender"], row["Nameset"], row["GivenName"], row["Surname"], row["Username"],row["Password"], row["permissionlevel"] ))

    def addLibrarian(self, newLibrarian):
        newLibrarian.id = str(len(self.personlist))
        self.personlist.append(newLibrarian)
        return newLibrarian

    def addSubcriber(self, newSubscriber):
        newSubscriber.id = str(len(self.personlist))
        self.personlist.append(newSubscriber)
        return newSubscriber
    

    def showSubscribers(self):
        onlysubscribers = []
        for i in self.personlist:
            if i.permissionLevel == 1:
                onlysubscribers.append(i)
        return onlysubscribers

    def showLibrarian(self):
        librarianlist = []
        for i in self.personlist:
            if i.permissionLevel == 0:
                librarianlist.append(i)
        return librarianlist

    def createBackup(self):
            with open('customerBackup.json', 'w') as json_file:
                dict_customer = []
                for i in self.personlist:
                    if i.permissionLevel == 1:
                        arr = {"Number": i.id,
                            "Gender": i.gender,
                            "Nameset": i.nameSet,
                            "GivenName": i.firstName,
                            "Surname": i.surname,
                            "StreetAddress": i.address,
                            "ZipCode": i.zipcode,
                            "City": i.city,
                            "EmailAddress": i.emailAddress,
                            "Username": i.username,
                            "TelephoneNumber": i.telephoneNumber,
                            "permissionlevel": i.permissionLevel
                            }
                        dict_customer.append(arr)
                    else:
                        arr= {"Number": i.id,
                            "Gender": i.gender,
                            "Nameset": i.nameSet,
                            "GivenName": i.firstName,
                            "Surname": i.surname,
                            "Username": i.username,
                            "Password": i.password,
                            "permissionlevel": i.permissionLevel
                        }
                        dict_customer.append(arr)

                json.dump(dict_customer, json_file)

    def restoreBackup(self):
        self.personlist = []
        try:
            self.addCustomersFromJsonFile("customerBackup.json")
        except:
            print("No backup found. Please make one first.")
