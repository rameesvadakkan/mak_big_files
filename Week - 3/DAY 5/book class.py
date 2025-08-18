class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def book_details(self):
        print(f"Book is{self.title} author is {self.author}")
        print(f"Book price is {self.price}")

book1 = Book("python Beginner","Ramees",100)
book1.book_details()