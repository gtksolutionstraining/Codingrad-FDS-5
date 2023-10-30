def login(LMS):
    username = input("Enter username:")
    password = input("Enter password:")
    status = False
    for user in LMS["ADMINS"]:
        if user["USERNAME"] == username \
            and user["PASSWORD"] == password:
            status = True
            break
        else:
            continue
    return status