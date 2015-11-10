'''
Created on Nov 8, 2015

@author: AlexandruD
'''
from Utils.Utilities import IdHandler

class Student(object):
    '''
    classdocs
    '''


    def __init__(self, name, id = -1,  studRepo = []):
        '''
        Constructor
        '''
        self.__name = name
        if(id == -1):
            self.__id = IdHandler.getStudID(studRepo)
        else:
            self.__id = id
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
        studArray =  ['''Student id: {}\n Student name: {}\n
'''.format(self.getID(), self.getName())]
        for discipline in self.__disciplines:
            studArray.append(discipline.displayDiscipline())
        return studArray
    
    def getDisciplines(self):
        return self.__disciplines
    
    def setDisciplines(self):
        return self.__disciplines
    
    
    def __eq__(self, other):
        if(self.getName() == other.getName()):
            return True
        return False