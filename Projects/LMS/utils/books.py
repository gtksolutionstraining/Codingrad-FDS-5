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

def add_book(LMS):
    book_name = input("Enter book name!\n")
    book_ssn = input("Enter book SSN!\n")
    display_branch()
    br_choice = validate_choice()
    branch = BRANCHES_MAP[br_choice]
    display_year()
    yr_choice = validate_choice()
    year = YEARS_MAP[yr_choice]
    display_sem()
    sem_choice = validate_choice()
    sem = SEMS_MAP[sem_choice]
    book = {
        "book_name": book_name,
        "book_ssn": book_ssn
    }
    LMS["BOOKS"][branch][year][sem].append(book)    

def update_book():
    pass

def delete_book():
    pass

def get_book():
    pass

def display_books():
    pass

def manage_books(LMS):
    status = True
    while status:
        display_books_menu()
        choice = validate_choice()
        if choice == 1:
            add_book(LMS)
        elif choice == 2:
            update_book()
        elif choice == 3:
            delete_book()
        elif choice == 4:  
            get_book()
        elif choice == 5:
            display_books()
        elif choice == 6:   
            status = False
            print("Exiting from BOOKs Menu!")
        else:
            print("Please select 1/2/3/4/5/6")