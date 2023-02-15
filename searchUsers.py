from user import *   
import twint
import os
import time

def searchUser(twitterUser):
    print(COLOR_YELLOW + "Ingrese el nombre del Usuario: " + COLOR_RESET)
    user = input()
    twitterUser.conf = twint.Config()
    twitterUser.userName = user
    twitterUser.conf.Username = twitterUser.userName
    twitterUser.fileName = "./tweets_"+twitterUser.userName+".json"
    twitterUser.conf.Output = twitterUser.fileName 
    twitterUser.conf.Limit = 10
    try:
        twint.run.Search(twitterUser.conf)
        time.sleep(5)
        os.system("clear")
    except:
        print("El usuario " + f"{COLOR_RED}{twitterUser.userName}{COLOR_RESET}" + " no existe\n")
        twitterUser.userName = "" 
    else:
        twitterUser.fileName = "./tweets_"+twitterUser.userName+".json"
        twitterUser.conf.Output = twitterUser.fileName
        os.remove(twitterUser.fileName)
        print("El usuario " + f"{COLOR_GREEN}{twitterUser.userName}{COLOR_RESET}" + " existe\n")
    return 1