from os import system
from user import *
from searchUsers import *
from searchNumTweets import *
from searchDateTweets import *
from searchWordInTweets import *
from searchTweets import *
from exit import *
import twint
import os
import time
     
        
def executeOption(option, twitterUser):
    functions = {
        1: searchUser,
        2: searchTweets,
        3: searchXtweets,
        4: searchDateTweets,
        5: searchWordInTweet,
        6: Exit
    }
    for key, value in functions.items():
        if(option < 1 or option > 6):
            print(COLOR_RED + "Opcion no valida" + COLOR_RESET)
            break
        elif(key == option and option != "6"):
            value(twitterUser)
        elif(key == option and option == "6"):
            value()
            break
    