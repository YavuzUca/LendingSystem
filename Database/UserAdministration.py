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
        if id in self.customerlist:
            return self.idGenerator()
        else:
            return id

    def addCustomer(self, firstname, surname, address, zipcode, city, emailaddress, username, telephonenumber,
                    id=idGenerator()):
        newCustomer = {"id": id, "firstname": firstname, "surname": surname, "address": address, "zipcode": zipcode,
                       "city": city, "email": emailaddress, "username": username, "phone number": telephonenumber}
        self.customerlist.append(newCustomer)

    def showsubscribers(self):
        onlysubscribers = []
        for i in self.customerlist:
            if i[self._permissionlevel] == 1:
                onlysubscribers.append(i)
        return onlysubscribers

    def showLibrarian(self):
        librarianlist = []
        for i in self.customerlist:
            if i[self._permissionlevel] == 0:
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