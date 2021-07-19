class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
        
    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print(" * " + book)

    def borrowBook(self, bookname):
        if bookname in self.books:
            print("you have been issued {bookname}. Please keep it safe and return it within 30 days")
            self.books.remove(bookname)
            return True

        else:
            print("Sorry, This book has already been issued tp someone else. Please wait until the book is returned")
            return False

    def returnBook(self, bookname):
        self.books.append(bookname)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")

class Student:
        
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book
    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book

if __name__ =="__main__":
    centralLibrary = Library(["Algorithms", "Data Structure", "Java","DBMS","Python"])
    student = Student()
    # centralLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = ''' =====Welcome to Central Library=====
        Please choose an option:
        1. Listing all the Books
        2. Request a book 
        3. Add/Return a book2
        4. Exit the library'''
        print(welcomeMsg)
    
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library! Have a great day ahead:")
            exit()
        else:
            print("Invalid Choice!")
           
        print(welcomeMsg)
        

    