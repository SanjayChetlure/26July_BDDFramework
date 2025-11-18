from configparser import ConfigParser

#this function is use to get data from config.ini file
#need to pass 2 parameters 1-categeory, 2-key
def read_configuration(categeory,key):
    cp=ConfigParser()
    cp.read("Configurations/config.ini")
    value=cp.get(categeory,key)
    return value