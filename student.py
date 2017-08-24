import datetime
import books
class student:
    studentId=0
    def __init__(self,studentId=1,name=""):
        if(student.studentId<=studentId):
            student.studentId=studentId
        self.name=name
        self.studentId=student.studentId
        self.issuedBooks={}
        self.fine=0
        student.studentId+=1

    def setStudent(self):
        print "please enter the following details of the students"
        self.name=raw_input("Name:").lower()

    def calculateFine(self,dateOfIssue):
        dateToday=datetime.datetime(input("enter today's year in YYYY format"), input("enter today's month in MM format"),input("enter today's date in DD fromat"))
        if((dateToday-dateOfIssue).days<=14):
            return 0
        else:
            return 2*((dateToday-dateOfIssue).days-14)


    def issueBook(self,book):
        if book.bookId in self.issuedBooks:
            # print "student already has issued the book"
            return
        if len(self.issuedBooks)==3:
            return
        # if book.quantityAvbl==0:
            # return

        print "book "+book.name+"issued to "+self.name
        dateOfIssue=datetime.datetime(input("enter the year in YYYY format"), input("enter the month in MM format"),input("enter the date in DD fromat"))
        self.issuedBooks[book.bookId]=dateOfIssue

    def returnBook(self,book):
        if book.bookId in self.issuedBooks:
            self.fine+=self.calculateFine(self.issuedBooks[book.bookId])
            self.issuedBooks.pop(book.bookId)
        else:
            print "book not issued"
    def payFine(self,amountPaid):
        print "the student has paid "+str(amountPaid)+"rs"
        if amountPaid<=self.fine:
            self.fine-=amountPaid
            print "the student has to pay"+str(self.fine)+"rs now"
        else:
            print "return change of "+str(amountPaid-self.fine)+"rs"
            self.fine=0


    def __str__(self):
        return ("*"*100)+"\nthe student deatils are as follows:"+"\nStudent Id:"+str(self.studentId)+"\nStudent Name:"+self.name+"\nissued books are"+str(self.issuedBooks)+"\nfine due is:"+str(self.fine)+" at rs 2 per extra day"
