def validate_choice():
    status = True
    while status:
        try:
            choice = int(input("Please select any of the above!\n"))
            status = False
        except ValueError as ve:
            print("Please enter number only!")
        except Exception as e:
            print(f"[ERROR]:{e}")
            print("OOPs, Something went wrong")
    return choice

def login(LMS):
    username = input("Enter username:")
    password = input("Enter password:")
    ## 1. implement the below 
    ## if username not in LMS[Admins]--> no user found!
    ## if username is there --> check password 
        ## if password is wrong 
            ## Incorrect Password
            ## 2 chances left to the user 
    ## 2. Username Case Insenstive and Password Case Sensitive
    ## 3. handle if the username is empty
    ## 4. 
    status = False
    for user in LMS["ADMINS"]:
        if user["USERNAME"].lower() == username.lower() \
            and user["PASSWORD"] == password:
            status = True
            break
        else:
            continue
    return status

def validate_user(LMS):
    ## User RollNumber and Name and other info
    ## LMS["USERS"][branch][year][sem] 
    ## return True/False status
    pass