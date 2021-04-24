class Addcat:
    def __init__(self):
        self.list_cat = []

    def setCat(self, catObj):
        catObj.id = len(self.list_cat) + 1
        self.list_cat.append(catObj)
