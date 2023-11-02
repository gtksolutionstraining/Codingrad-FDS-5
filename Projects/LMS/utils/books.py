from utils.display import (
    display_year,
    display_sem,
    display_branch
)
from utils.validate import validate_choice
from commons.config import (
    YEARS_MAP,
    SEMS_MAP,
    BRANCHES_MAP
)

def display_books_menu():
    print("BOOKs Menu:")
    print("1. Adding a Book")
    print("2. Updating a Book")
    print("3. Deleting a Book")
    print("4. Get a Book")
    print("5. Display all Books")
    print("6. Exit")

def get_choice(map):
    status = True
    while status:
        br_choice = validate_choice()
        if br_choice in map.keys():
            status = False
        else:
            print(f"Please select any of these {list(map.keys())}")
    return br_choice

def get_info():
    display_branch()
    br_choice = get_choice(BRANCHES_MAP)
    branch = BRANCHES_MAP[br_choice]
    display_year()
    yr_choice = get_choice(YEARS_MAP)
    year = YEARS_MAP[yr_choice]
    display_sem()
    sem_choice = get_choice(SEMS_MAP)
    sem = SEMS_MAP[sem_choice]
    return branch,year,sem

def add_book(LMS):
    book_name = input("Enter book name!\n")
    book_ssn = input("Enter book SSN!\n")
    branch,year,sem = get_info()
    book = {
        "book_name": book_name,
        "book_ssn": book_ssn
    }
    LMS["BOOKS"][branch][year][sem].append(book)    
    print("Book added")

def update_book(LMS):
    branch,year,sem = get_info()
    book_ssn = input("Enter Book SSN")
    books = LMS["BOOKS"][branch][year][sem]
    book_ssns = list(map(lambda x:x['book_ssn'],books))
    if book_ssn in book_ssns:
        book_name = input("Enter new name for book: ")
        book = list(filter(lambda x:x['book_ssn']==book_ssn,books))[0]
        LMS["BOOKS"][branch][year][sem].remove(book)
        book['book_name'] = book_name
        LMS["BOOKS"][branch][year][sem].append(book)
        print("Book is updated")
    else:
        print("Book is not found")

def delete_book(LMS):
    branch,year,sem = get_info()
    book_ssn = input("Enter book ssn: ")
    books = LMS["BOOKS"][branch][year][sem]
    book_ssns = list(map(lambda x:x['book_ssn'],books))
    if book_ssn in book_ssns:
        book = books[book_ssns.index(book_ssn)]
        LMS["BOOKS"][branch][year][sem].remove(book)
        print(f"Book {book} deteled!")
    else:
        print("No Book found with given details.")

def get_book(LMS):
    ## validate user from users.py
    branch,year,sem = get_info()
    book_name = input("Enter book name: ")
    books = LMS["BOOKS"][branch][year][sem]
    book_names = list(map(lambda x:x['book_name'],books))
    if book_name in book_names:
        ind = book_names.index(book_name)
        book = books[ind]
        print(f"Please take your book: {book}")
        LMS["BOOKS"][branch][year][sem].remove(book)
    else:
        print("No book, please visit again...!")

def display_books(LMS):
    branch,year,sem = get_info()
    print("Books:")
    ## print it nice manner
    print(LMS["BOOKS"][branch][year][sem])

def manage_books(LMS):
    status = True
    while status:
        display_books_menu()
        choice = validate_choice()
        if choice == 1:
            add_book(LMS)
        elif choice == 2:
            update_book(LMS)
        elif choice == 3:
            delete_book(LMS)
        elif choice == 4:  
            get_book(LMS)
        elif choice == 5:
            display_books(LMS)
        elif choice == 6:   
            status = False
            print("Exiting from BOOKs Menu!")
        else:
            print("Please select 1/2/3/4/5/6")