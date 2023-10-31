"""
main.py:
    This is a starting point for the LMS
Authors: tharunkumargoka2020@gmail.com
"""
import sys
sys.path.append("/Users/gtk/GTK/CodinGrad/Codingrad-FDS-5/Projects/LMS/")
from assets.data import LMS
from utils.display import display_lms
from utils.validate import login

def main():
    """main
    This is a starting function for LMS
    Arguments:
    Returns:
    """
    print("*"*25)
    print("Welcome to LMS!")
    print("*"*25)
    status = login(LMS)
    if status:
        print("Authentication Successfull..!")
        display_lms(LMS)
    else:
        print("Authentication Failure...!")
   
if __name__ == "__main__":
    main()