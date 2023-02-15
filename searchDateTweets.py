from user import *   
import twint
import os
import time

def searchDateTweets(twitterUser):
    if (twitterUser.userName == None):
        print(COLOR_RED+"No se ha seleccionado un usuario"+COLOR_RESET)
    else:
        if (os.path.exists(twitterUser.fileName) == True):
            os.remove(twitterUser.fileName)
        twitterUser.resetUserConf()
        print(COLOR_YELLOW + "Ingrese la fecha que quiere capturar los tweets(e.j. 2000-12-27): " + COLOR_RESET)
        fecha = input()
        twitterUser.conf.Since = fecha + " 00:00:00"
        twitterUser.conf.Until = fecha + " 23:59:59"
        twint.run.Search(twitterUser.conf)
        time.sleep(2)
        os.system("clear")
        print(COLOR_GREEN+"Se generó el informe correctamente"+COLOR_RESET)
        return 0