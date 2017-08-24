import functions
import books
import student as students
import os

os.system("clear")

print "welcome to the library management system\n press any key to continue........"
a=raw_input()
os.system("clear")

while True:
    os.system("clear")

    print """
please choose from the following options:
    1.Read Details of all Books
    2.Read Details of all Students
    3.Search for a Book
    4.Search for a Student
    5.Issue Book
    6.Return Book
    7.Delete Book
    8.Pay Fine
    9.Add Student
    10.Add Book
    11.Delete student
    12.find by ISBN or ID
    13.EXIT
    """
    try:
        optionChosen=int(raw_input())
    except:
        print "sorry wrong input entered please enter again"
        # a=raw_input()
        optionChosen=20000
    if optionChosen==13:
        break
        os.system("clear")
    elif optionChosen==1:
        os.system("clear")
        functions.showBookData()
        print "press any key to go bak to menu......."
        a=raw_input()
    elif optionChosen==2:
        os.system("clear")
        functions.showStudentData()
        print "press any key to go bak to menu......."
        a=raw_input()
    elif optionChosen==3:
        os.system("clear")
        bookQuery=raw_input("enter Query to search book")
        booksFound=functions.TrySearchingBook(bookQuery)
        if booksFound==[]:
            print "sorry no books were found"
        else:
            print "books found are:"
            for i in booksFound:
                print i
        print "press any key to go back to menu......."
        a=raw_input()
    elif optionChosen==4:
        os.system("clear")
        stuQuery=raw_input("enter studentId to search student")
        try:
            obj=functions.findstudent(stuQuery)
            if(obj==None):
                raise ValueError
            print obj
        except:
            if obj!=None:
                print "an error occured"

        print "press any key to go back to menu......."
        a=raw_input()
    elif optionChosen==5:
        os.system("clear")
        studentId=raw_input("ENTER THE STUDENT ID")
        bookId=raw_input("ENTER THE BOOK ID")
        functions.issueBook(studentId, bookId)
        print "press any key to go back to menu......."
        a=raw_input()
    elif optionChosen==6:
        os.system("clear")
        studentId=raw_input("ENTER THE STUDENT ID")
        bookId=raw_input("ENTER THE BOOK ID")
        functions.returnBook(studentId, bookId)
        print "press any key to go back to menu......."
        a=raw_input()
    elif optionChosen==7:
        os.system("clear")
        bookId=raw_input("ENTER THE BOOK ID")
        # print "delete book function to be made"
        functions.deleteBook(bookId)
        print "press any key to go back to menu......."
        a=raw_input()
    elif optionChosen==8:
        os.system("clear")
        studentId=raw_input("ENTER THE STUDENT ID")
        functions.payFine(studentId)
        print "press any key to go back to menu......."
        a=raw_input()
    elif optionChosen==9:
        os.system("clear")
        functions.enterStudent()
        print "press any key to go back to menu......."
        a=raw_input()
    elif optionChosen==10:
        os.system("clear")
        functions.enterBook()
        print "press any key to go back to menu......."
        a=raw_input()
    elif optionChosen==11:# TODO: delete student
        os.system("clear")
        sid=input("enter the id of student to be deleted")
        functions.deleteStudent(sid)
        print "press any key to go back to menu......."
        a=raw_input()
    elif optionChosen==12:
        os.system("clear")
        idOrIsbn=raw_input("enter the ISBN or ID of the book")
        book=functions.findBook(idOrIsbn)
        if book!=None:
            print book
        print "press any key to go back to menu......."
        a=raw_input()
    else:
        os.system("clear")
        print "please enter a valid option"
        print "press any key to go back to menu......."
        a=raw_input()
