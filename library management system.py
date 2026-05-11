
class Book:

    def __init__(self, title , author):
        self.title = title
        self.author = author
        self.is_available = True

    def display_info(self):
        if self.is_available:
            status = "available"
        else:
            status = "not available"

        print(f" title: {self.title}\n author: {self.author}\n availability: {status} ")

class Library:

    def __init__(self):
        self.book_list = []

    def add_book(self):
        title = input("enter the title of book:")
        author = input("enter the author name:")

        new_book = Book(title, author)
        self.book_list.append(new_book)
        print ("Book is succussfully added")

    def view_books(self):
        if not self.book_list:
            print("list is empty")
            return
        else:
            print("The list of books")
            for books in self.book_list:
                books.display_info()
                print("---------------------")


    def search_book(self):
        title = input("Enter the book title:").lower()
        found = False

        for book in self.book_list:
            if title == book.title.lower():
                print (f"{title} is available")
                book.display_info()
                found = True

        if not found:
            print (f"{title} is not available")


my_library = Library()

while True:

    print("\t--- Liabrary Management System---")
    print(" 1:  Add_Books ")
    print(" 2:  View_Books ")
    print(" 3:  search_Book")
    print(" 4:  Exit ")

    user_choice = int(input("Enter the choice (1, 2, 3, 4): "))
    if user_choice not in [1, 2, 3]:
        print ("invalid user choice")
        continue

    if user_choice == 1:
        my_library.add_book()

    elif user_choice == 2:
        my_library.view_books()

    elif user_choice == 3:
        my_library.search_book()

    elif user_choice == 4:
        break

    else:
        print ("you are enter wrong choice, Plz Enter valid choice")


        


        