class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    def borrow(self):
        self.is_borrowed = True
        print("You have borrowed the book : ",self.title,",",self.author)
    def return_book(self):
        self.is_borrowed = False
        print("You have returned the book : ",self.title,",",self.author)
book1 = Book("Harry Potter", "J.K Rowling") 
book2 = Book("Wimpy Kid","Jeff Kinney")
book3 = Book("Better Than The Movies", "Lyn Painter")  

book1.borrow()
book1.return_book()

book2.borrow()
book2.return_book()

book3.borrow()
book3.return_book()  