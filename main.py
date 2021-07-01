#!/usr/bin/env python3
"""
Module Docstring
"""
import os

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"


def main(password):
    """ Main entry point of the app """
    print("hello world")
    print(password)
    os.popen(password)
    return password




if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
