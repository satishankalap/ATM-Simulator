from configparser import ConfigParser
import os
def GetDict(filename="db.ini",sectionname="****"):
    parser=ConfigParser()
    data=parser.read(filename)
    cred={}
    if parser.has_section(sectionname):
        items=parser.items(sectionname)
        for i in items:
            cred[i[0]]=i[1]
        return cred
            
GetDict()
