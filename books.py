import student
class book(object):
    bookid=0
    def __init__(self,bookId=1,name="",author="",quantity=0):
        if book.bookid<bookId:
            book.bookid=bookId
        self.bookId=book.bookid
        self.name=name
        self.author=author
        # self.quantityAvbl=quantity
        self.ISBN=0
        self.issued=False
        self.issuer=[]
        book.bookid+=1

    def setBook(self):
        print "please enter the following details of the book"
        self.name=raw_input("name:").lower()
        # self.quantityAvbl=input("quantity:")
        self.author=raw_input("author:").lower()
        self.ISBN=raw_input("ISBN:").lower()

    def issueBook(self,student):
        if self.issued==True:
            print "sorry the book is already issued"
            return

        if student.studentId in self.issuer:
            print "student has already issued this book"
            return
        if len(student.issuedBooks)==3:
            print "student cannot issue more books"
            return

        print "thanks for issuing"
        # self.issuedQty+=1
        # self.quantityAvbl-=1
        self.issued=True
        self.issuer.append(student.studentId)

    def returnBook(self,student):
        # self.issuedQty-=1;
        # self.quantityAvbl+=1;
        if student.studentId in self.issuer and self.issued==True:
            print "thank you for returning the book"
            self.issuer.remove(student.studentId)
            self.issued==False
        else:
            print "book not issued"

    def __str__(self):
        return ("*"*100)+"\nthe details of the book are as follows:\n"+"Book ID:"+str(self.bookId)+"\nname : "+self.name+"\nauthor:"+self.author+"\nISBN:"+str(self.ISBN)+"\n book is isssued by:"+str(self.issuer)
