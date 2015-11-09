'''
Created on Nov 8, 2015

@author: AlexandruD
'''
from Utils.Utilities import IdHandler

class Student(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        self.__name = name
        self.__id = IdHandler.getStudID()
        self.__disciplines = []
        
    def setID(self, ID):
        self.__id = ID
        
    def getID(self):
        return self.__id
    
    def addDiscipline(self, discipline):
        self.__disciplines.append(discipline)