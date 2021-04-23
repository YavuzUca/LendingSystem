class Book:
    def __init__(self, title, author, ISBN, country, language, link, image_link, pages, year):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.country = country
        self.language = language
        self.link = link
        self.image_link = image_link
        self.pages = pages
        self.year = year
        self.list_book = []

    def update(self, obj):
        obj.id = len(self.list_book) + 1
        self.list_book.append(obj)
