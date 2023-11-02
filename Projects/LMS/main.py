"""
main.py:
    This is a starting point for the LMS
Authors: tharunkumargoka2020@gmail.com
"""
import sys
from commons.config import DATA_PATH
from utils.lms import display_lms
from utils.validate import login
from utils.file import (
    read_data,
    write_data
)

sys.path.append("/Users/gtk/GTK/CodinGrad/Codingrad-FDS-5/Projects/LMS/")


def main():
    """main
    This is a starting function for LMS
    Arguments:
    Returns:
    """
    print("*"*25)
    print("Welcome to LMS!")
    print("*"*25)
    LMS = read_data(DATA_PATH)
    status = login(LMS)
    if status:
        print("Authentication Successfull..!")
        display_lms(LMS)
        write_data(LMS,DATA_PATH)
    else:
        print("Authentication Failure...!")
   
if __name__ == "__main__":
    main()