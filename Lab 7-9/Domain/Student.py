'''
Created on Nov 8, 2015

@author: AlexandruD
'''
from Utils.Utilities import IdHandler

class Student(object):
    '''
    classdocs
    '''


    def __init__(self, name, studRepo = []):
        '''
        Constructor
        '''
        self.__name = name
        self.__id = IdHandler.getStudID(studRepo)
        self.__disciplines = []
        
    def setID(self, ID):
        self.__id = ID
        
    def getID(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def addDiscipline(self, discipline):
        self.__disciplines.append(discipline)
        
    def displayStudent(self):
        studArray =  ['''Student id: {} Student name: {}
'''.format(self.getID(), self.getName())]
        for discipline in self.__disciplines:
            studArray.append(discipline.displayDiscipline())
        return studArray