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


def display_lms():
    status = True
    while status:
        print("LMS Menu:")
        print("1. BOOKS")
        print("2. USERS")
        print("3. Exit")
        choice = int(input("Please select any of the above!"))
        if choice == 1:
            print("Showing BOOKs Menu")
        elif choice == 2:
            print("Showing USERS Menu")
        elif choice == 3:
            print("Exiting..!")
            status = False
        else:
            print("Wrong Input....Please select 1/2/3..!")