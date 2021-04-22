import csv
import json, random


class UserAdministration:
    customerlist = []

    def addCustomersFromFile(self, File):
        with open(File, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.customerlist.append(row)

    def idGenerator(self):
        id = str(random.randint(1, 1000000))
        while len(id) < 7:
            id = '0' + id
        #
        # for i in self.customerlist:
        #     if id == i.id:
        #         return self.idGenerator()
        return id

    def addCustomer(self, obj):
        newCustomer = {"id": self.idGenerator(),
                       "firstname": obj.firstName,
                       "surname": obj.surname,
                       "address": obj.address,
                       "zipcode": obj.zipcode,
                       "city": obj.city,
                       "email": obj.emailAddress,
                       "username": obj.username,
                       "phone number": obj.telephoneNumber,
                       "perms": obj.permissionLevel}

        self.customerlist.append(newCustomer)

    def showsubscribers(self):
        onlysubscribers = []
        for i in self.customerlist:
            if i["perms"] == 1:
                onlysubscribers.append(i)
        return onlysubscribers

    def showLibrarian(self):
        librarianlist = []
        for i in self.customerlist:
            if i["perms"] == 0:
                librarianlist.append(i)
        return librarianlist

    def createBackup(self):
        with open('customerBackup.json') as json_file:
            json.dump(self.customerlist, json_file)

    def restoreBackup(self):
        try:
            self.addCustomersFromFile("customerBackup.json")
        except:
            print("No backup found. Please make one first.")
