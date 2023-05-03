import configparser

config = configparser.RawConfigParser()
config.read(".\\Configeration\\config.ini")


class Read_Congig:

    @staticmethod
    def getApplicationURL():
        url = config.get('Common Info', 'baseURL')
        return url

    @staticmethod
    def getUserName():
        userName = config.get('Common Info', 'userName')
        return userName

    @staticmethod
    def getPassword():
        password = config.get('Common Info', 'password')
        return password