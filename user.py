COLOR_RED = "\033[1;31m"
COLOR_GREEN = "\033[1;32m"
COLOR_YELLOW = "\033[1;33m"
COLOR_BLUE = "\033[1;34m"
COLOR_RESET = "\033[0;m"


class User:
    def __init__(self):
        self.userName = None
        self.conf = None
        self.fileName = ""
        
    def resetUserConf(self):
        self.conf.Filter_retweets = False
        self.conf.Min_likes = 0
        self.conf.Min_replies = 0
        self.conf.Min_retweets = 0
        self.conf.Limit = 10000
        self.conf.Search = None
        self.conf.Since = None
        self.conf.Until = None
        