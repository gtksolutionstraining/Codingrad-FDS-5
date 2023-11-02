from utils.display import display_lms_menu
from utils.validate import validate_choice
from utils.books import manage_books

def display_lms(LMS):
    status = True
    while status:
        display_lms_menu()
        choice = validate_choice()
        if choice == 1:
            manage_books(LMS)
        elif choice == 2:
            print("Showing USERS Menu")
        elif choice == 3:
            print("Logging out..!")
            print("Thank you!")
            status = False
        else:
            print("Wrong Input....Please select 1/2/3..!")