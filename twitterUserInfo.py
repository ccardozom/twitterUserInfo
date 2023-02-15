from printOptions import printMenu
from execute import *
from user import User        
import sys


exit = "6"

def main():
    twitterUser = User()
    option = None

    while option != exit:
        printMenu()
        option = int(input())
        system("clear")
        executeOption(option, twitterUser)


if __name__ == '__main__':
    sys.exit(main())
    