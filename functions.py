import pickle
import books
import student as students
import os

def enterBook():
    file=open("book.bin","ab+")
    IDstorage=open("BookId.bin","ab+")
    id=int(pickle.load(IDstorage))
    id+=1
    book=books.book(id)
    book.setBook()
    pickle.dump(book, file)
    IDstorage.close()
    IDstorage=open("BookId.bin","wb+")
    pickle.dump(id, IDstorage)
    IDstorage.close()


def enterStudent():
    file=open("student.bin","ab+")
    IDstorage=open("StuId.bin","ab+")
    id=int(pickle.load(IDstorage))
    id+=1
    # book=books.book(id)
    student=students.student(id)
    student.setStudent()
    pickle.dump(student, file)
    IDstorage.close()
    IDstorage=open("StuId.bin","wb+")
    pickle.dump(id, IDstorage)
    IDstorage.close()

def showBookData():
    file=open("book.bin", "ab+")
    print "this is the book database of the library"
    print "the data is:"
    print "BOOK ID\t"+"| BOOK ISBN\t"+"| BOOK NAME\t"+"| AUTHOR\t"+"| issued?"
    print ("*"*50)
    array=[]
    while True:
        try:
            bookObj=pickle.load(file)
            # print str(bookObj.bookId)+"\t|"+str(bookObj.ISBN)+"\t|"+bookObj.name+"\t|"+bookObj.author
            array.append(bookObj)
        except EOFError:
            print ("*"*50)
            file.close()
            break
    def funn(x):
        return x.ISBN
    array.sort(key=funn)
    for bookObj in array:
        print str(bookObj.bookId)+"\t|"+str(bookObj.ISBN)+"\t|"+bookObj.name+"\t|"+bookObj.author+"\t|"+str(bookObj.issued)



def showStudentData():
    file=open("student.bin", "ab+")
    print "this is the student database of the library"
    print "the data is:"
    print "STUDENT ID"+"| STUDENT NAME"
    while True:
        try:
            studentObj=pickle.load(file)
            print str(studentObj.studentId)+"\t|"+studentObj.name
        except EOFError:
            print ("*"*50)+"this is it"
            file.close()
            break


def findBook(bookIdOrName):
    file=open("book.bin","ab+")
    while True:
        try:
            obj=pickle.load(file)
            if str(obj.bookId)==str(bookIdOrName) or obj.ISBN==bookIdOrName:
                return obj
        except EOFError:
            print "sorry the book was not found in the database"
            return None


def findstudent(studentIdOrName):
    file=open("student.bin","ab+")
    while True:
        try:
            obj=pickle.load(file)
            if str(obj.studentId)==str(studentIdOrName) or obj.name==studentIdOrName:
                return obj
        except EOFError:
            print "sorry the student was not found in the database"
            return None

def issueBook(studentIdOrName,bookIdOrName):
    stuFile=open("student.bin", "ab+")
    bookFile=open("book.bin", "ab+")
    stuNew=open("stu2.bin", "ab+")
    bookNew=open("book2.bin", "ab+")
    stuobj=findstudent(studentIdOrName);
    bookobj=findBook(bookIdOrName);
    if bookobj!=None and stuobj!=None:
        bookobj.issueBook(stuobj)
        stuobj.issueBook(bookobj)
    else:
        return
    while True:
        try:
            student=pickle.load(stuFile)
            if str(student.studentId)!=str(studentIdOrName) and student.name!=studentIdOrName:
                pickle.dump(student, stuNew)
        except EOFError:
            break
    while True:
        try:
            book=pickle.load(bookFile)
            if str(book.bookId)!=str(bookIdOrName) and book.name!=bookIdOrName:
                pickle.dump(book, bookNew)
        except EOFError:
            break
    pickle.dump(stuobj, stuNew)
    pickle.dump(bookobj, bookNew)
    bookFile.close()
    stuFile.close()
    stuNew.close()
    bookNew.close()
    os.rename("stu2.bin", "student.bin")
    os.rename("book2.bin", "book.bin")
def returnBook(studentIdOrName,bookIdOrName):
    stuFile=open("student.bin", "ab+")
    bookFile=open("book.bin", "ab+")
    stuNew=open("stu2.bin", "ab+")
    bookNew=open("book2.bin", "ab+")
    stuobj=findstudent(studentIdOrName);
    bookobj=findBook(bookIdOrName);
    if bookobj!=None and stuobj!=None:
        bookobj.returnBook(stuobj)
        stuobj.returnBook(bookobj)
    else:
        return
    while True:
        try:
            student=pickle.load(stuFile)
            if str(student.studentId)!=str(studentIdOrName) and student.name!=studentIdOrName:
                pickle.dump(student, stuNew)
        except EOFError:
            break
    while True:
        try:
            book=pickle.load(bookFile)
            if str(book.bookId)!=str(bookIdOrName) and book.name!=bookIdOrName:
                pickle.dump(book, bookNew)
        except EOFError:
            break
    print  "the student ha to pay "+str(stuobj.fine)+"rs"
    pickle.dump(stuobj, stuNew)
    pickle.dump(bookobj, bookNew)
    bookFile.close()
    stuFile.close()
    stuNew.close()
    bookNew.close()
    os.rename("stu2.bin", "student.bin")
    os.rename("book2.bin", "book.bin")
def payFine(studentId):
    stuFile=open("student.bin", "ab+")
    stuNew=open("stu2.bin", "ab+")
    stuobj=findstudent(studentId);
    while True:
        try:
            student=pickle.load(stuFile)
            if str(student.studentId)!=str(studentId) and student.name!=studentId:
                pickle.dump(student, stuNew)
        except EOFError:
            break
    print  "the student has to pay a fine of "+str(stuobj.fine)+"rs"
    amountPaid=input("enter the amount given by student")
    stuobj.payFine(amountPaid)
    pickle.dump(stuobj, stuNew)
    stuFile.close()
    stuNew.close()
    os.rename("stu2.bin", "student.bin")
def TrySearchingBook(searchQuery):
    queryArr=searchQuery.lower().split()
    if queryArr==[]:
        print "empty query"
        return []
    resultArr=[]
    bookFile=open("book.bin","ab+")
    while True:
        try:
            bookObj=pickle.load(bookFile)
            i=queryArr[0]
            if i in bookObj.name or i in bookObj.author:
                resultArr.append(bookObj)
        except EOFError:
            bookFile.close()
            break
    # for i in xrange(1,len(queryArr)):
    i=0
    while resultArr!=[] and  i<len(queryArr):
        for obj in resultArr:
            if queryArr[i] not in obj.name and  queryArr[i] not in obj.author:
                resultArr.pop(resultArr.index(obj))
        i+=1
    return resultArr
def deleteStudent(studentId):
    stuFile=open("student.bin", "ab+")
    stuNew=open("stu2.bin", "ab+")
    stuobj=findstudent(studentId);
    if stuobj==None:
        return
    if(stuobj.fine==0 and stuobj.issuedBooks=={}):
        print "deleted student is:"
        print stuobj

    else:
        pickle.dump(stuobj,stuNew)
        print "student cannot be deleted he/she has books issued or fines to be payed"

    while True:
        try:
            student=pickle.load(stuFile)
            if str(student.studentId)!=str(studentId) and student.name!=studentId:
                pickle.dump(student, stuNew)
        except EOFError:
            break

    stuFile.close()
    stuNew.close()
    os.rename("stu2.bin", "student.bin")
def deleteBook(bookId):
    bookFile=open("book.bin", "ab+")
    bookNew=open("book2.bin", "ab+")
    bookobj=findBook(bookId);
    if bookobj==None:
        return
    if(bookobj.issued==False):
        print "deleted book is:"
        print bookobj

    else:
        pickle.dump(bookobj,bookNew)
        print "book cannot be deleted it is currently issued by a student"
    while True:
        try:
            book=pickle.load(bookFile)
            if str(book.bookId)!=str(bookId):
                pickle.dump(book, bookNew)
        except EOFError:
            break

    bookFile.close()
    bookNew.close()
    os.rename("book2.bin", "book.bin")

# deleteStudent(2)


# a=TrySearchingBook("ciorth")
# a=map(str,a)
# print a
