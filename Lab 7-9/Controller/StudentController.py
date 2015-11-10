'''
Created on Nov 8, 2015

@author: AlexandruD
'''

class StudentController(object):
    '''
    classdocs
    '''


    def __init__(self, studRepo):
        '''
        Constructor
        '''
        self.__studRepo = studRepo
    
    def addStud(self, student):
        studList = []
        studList.append(student)
        self.__studRepo.addStudents(studList)
    
    def addStudent(self, studentName, studID = -1):
        self.__studRepo.addStudent(studentName, studID)
        
    def displayStudents(self):
        return self.__studRepo.displayStudents()
    
    def fetchFromFile(self):
        return self.__studRepo.fetchFromFile()
    
    def getFile(self):
        return self.__studRepo.getFile()