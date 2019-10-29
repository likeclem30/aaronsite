import datetime
""" This script create empty file """

filename = datetime.datetime.now()
def createfile():
    """ This function create an empty file"""
    with open(filename.strftime('%Y-%m-%d-%H-%M')+'.txt','w') as file:
        file.write("")

createfile()