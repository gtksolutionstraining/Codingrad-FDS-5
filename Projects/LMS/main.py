"""
main.py:
    This is a starting point for the LMS
"""
import sys
sys.path.append("/Users/gtk/GTK/CodinGrad/Codingrad-FDS-5/Projects/LMS/")
from assets.data import LMS

def main():
    print("*"*25)
    print("Welcome to LMS!")
    print("*"*25)
    print("LMS Library is: ")
    print(LMS)
    # branches = LMS["BOOKS"]
    # years = 


if __name__ == "__main__":
    main()