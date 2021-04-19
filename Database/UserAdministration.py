import json, random

class UserAdministration:

    customerlist = []

    def addCustomersFromFile(self, File):
        with open(File) as json_file:
            customerlist = json.loads(json_file)
            return customerlist

    def idGenerator(self):
            id = str(random.randint(1,1000000))
            while len(id) < 7:
                id = '0' + id
            if id in self.customerlist:
                return self.idGenerator()
            else:
                return id
    
    def addCustomer(self, firstname, surname, address, zipcode, city, emailaddress, username, telephonenumber, id = idGenerator()):
        newCustomer = {"id":id, "firstname": firstname, "surname": surname, "address": address, "zipcode": zipcode, "city": city, "email": emailaddress, "username": username, "phone number": telephonenumber}
        
        with open('thajsonfile', 'a') as json_file:
            json.dumps(newCustomer, json_file)

    
    def showsubscribers(self):
        for i in self.customerlist:
            if i[self._permissionlevel] == 1:
                print("Name:", i['firstname'] + ' ' + i['surname'])

    def showLibrarian(self):
        for i in self.customerlist:
            if i[self._permissionlevel] == 0:
                print("this is the librarian account.")

    def createBackup(self):
        with open('customerBackup.json') as json_file:
             json.dump(self.customerlist, json_file)

    def restoreBackup(self):
        try: 
            self.addCustomersFromFile("customerBackup.json")
        except:
            print("No backup found. Please make one first.")