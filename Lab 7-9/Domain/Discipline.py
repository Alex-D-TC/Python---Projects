'''
Created on Nov 8, 2015

@author: AlexandruD
'''
from Utils.Utilities import IdHandler

class Discipline(object):
    '''
    classdocs
    '''


    def __init__(self, name, teacher, discID = -1, discRepo = []):
        '''
        Constructor
        '''
        self.__name = name
        if(discID == -1):
            self.__id = IdHandler.getDiscID(discRepo)
        else:
            self.__id = discID
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
    
    def getGradeString(self):
        gradeString = ''
        if(self.__grades != []):
            gradeString = gradeString + 'Grades: '
            for grade in self.__grades:
                gradeString = gradeString + str(grade) + ','
        gradeString = gradeString[:len(gradeString) - 1]
        return gradeString + '\n'
    
    def addGrade(self, grade):
        try: gradeCount = len(grade)
        except TypeError: gradeCount = 0
        if(gradeCount == 0):
            self.__grades.append(grade)
        else:
            for i in range(0, len(grade)):
                self.__grades.append(grade[i])
                
    def displayDiscipline(self):
        discString = ''' Discipline id: {}\n Discipline name: {}\n Discipline teacher: {}\n Grades: {}'''.format(self.getID(), self.getName(), self.getTeacher(), self.getGradeString())
        
        discString = discString[:len(discString)-1]
        discString = discString + '\n'
        return discString

    def __eq__(self, other):
        if(self.getName() == other.getName()):
            if(self.getTeacher() == other.getTeacher()):
                return True
        return False