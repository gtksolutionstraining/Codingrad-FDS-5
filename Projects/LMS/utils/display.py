from commons.config import(
    YEARS,
    SEMS,
    BRANCHES
)
def display_books(LMS):
    for book,bookValues in LMS.items():
        print(book)
        for branch, branchValues in bookValues.items():
            print(f"\t{branch}")
            for year, yearValues in branchValues.items():
                print(f"\t\t{year}")
                for sem,semValues in yearValues.items():
                    print(f"\t\t\t{sem}:{semValues}")

# def display_books_menu():
#     status= True
#     while status:
#         print("BOOKs Menu:")
#         print("1. Adding a Book")
#         print("2. Deleting a Book")
#         print("3. Updating a Book")
#         print("4. Get a Book")
#         print("5. Get all Books")
#         choice = int(input("Please select any of the above!"))
#         if choice == 1:
#             print("")
        # elif choice == 2:
        #     print("Showing USERS Menu")
        # elif choice == 3:
        #     print("Exiting..!")
        #     status = False
        # else:
        #     print("Wrong Input....Please select 1/2/3..!")

def display_lms_menu():
    print("LMS Menu:")
    print("1. BOOKS")
    print("2. USERS")
    print("3. Logout")

def display_year():
    print("Years:")
    i = 1
    for year in YEARS:
        print(f"{i}: {year}")
        i += 1

def display_sem():
    print("Semesters:")
    i = 1
    for sem in SEMS:
        print(f"{i}: {sem}")
        i += 1

def display_branch():
    print("Branches:")
    i = 1
    for branch in BRANCHES:
        print(f"{i}: {branch}")
        i += 1