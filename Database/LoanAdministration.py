import json


class LoanAdministration:
    def __init__(self):
        self.borrowedBooks = []
    
    def update(self, Loanitem):
        self.borrowedBooks.append(Loanitem)

    def createBackup(self):
        with open('borrowedbooksBackup.json', 'w') as json_file:
              json.dump(self.borrowedBooks, json_file)

    def restoreBackup(self):
        try: 
            with open ('borrowedbooksBackup.json') as json_file:
                self.borrowedbooks = json.load(json_file)
        except:
            print("No backup found. Please make one first.")