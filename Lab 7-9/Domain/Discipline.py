'''
Created on Nov 8, 2015

@author: AlexandruD
'''
from Utils.Utilities import IdHandler

class Discipline(object):
    '''
    classdocs
    '''


    def __init__(self, name, teacher, discRepo = []):
        '''
        Constructor
        '''
        self.__name = name
        self.__id = IdHandler.getDiscID(discRepo)
        self.__teacher = teacher
        self.__grades = []
        
    def setID(self, ID):
        self.__id = ID
        
    def getID(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getTeacher(self):
        return self.__teacher
    
    def getGrades(self):
        return self.__grades
    
    def addGrade(self, grade):
        try: gradeCount = len(grade)
        except ValueError: gradeCount = 0
        if(gradeCount == 0):
            self.__grades.append(grade)
        else:
            for i in range(0, len(grade)):
                self.__grades.append(grade[i])
                
    def displayDiscipline(self):
        return '''Discipline id: {} Discipline name: {} Discipline teacher: {}
'''.format(self.getID(), self.getName(), self.getTeacher())