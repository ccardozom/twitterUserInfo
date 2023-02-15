from user import *   
import twint
import os
import time

def searchXtweets(twitterUser):
    if (twitterUser.userName == None):
        print(COLOR_RED+"No se ha seleccionado un usuario"+COLOR_RESET)
    else:
        if (os.path.exists(twitterUser.fileName) == True):
            os.remove(twitterUser.fileName)
        twitterUser.resetUserConf()
        print(COLOR_YELLOW + "Ingrese el número de tweets que quieres capturar: " + COLOR_RESET)
        limit = input()
        twitterUser.conf.Limit = limit
        twint.run.Search(twitterUser.conf)
        time.sleep(2)
        os.system("clear")
        print(COLOR_GREEN+"Se generó el informe correctamente"+COLOR_RESET)
        return 0
    return 0