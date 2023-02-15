from user import *   
import twint
import os
import time

def searchTweets(twitterUser):
    if (twitterUser.userName == None):
        print(COLOR_RED+"No se ha seleccionado un usuario"+COLOR_RESET)
    else:
        if (os.path.exists(twitterUser.fileName) == True):
            os.remove(twitterUser.fileName)
        twitterUser.resetUserConf()
        twint.run.Search(twitterUser.conf)
        time.sleep(5)
        os.system("clear")
        print(COLOR_GREEN+"Se generó el informe correctamente"+COLOR_RESET)
        return 0