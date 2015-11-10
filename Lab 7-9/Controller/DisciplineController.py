'''
Created on Nov 8, 2015

@author: AlexandruD
'''
from Utils.Utilities import Validator

class DisciplineController(object):
    '''
    classdocs
    '''


    def __init__(self, discRepo):
        '''
        Constructor
        '''
        self.__discRepo = discRepo
    
    def toDisciplineByID(self, disc, disciplineList):
        discID = Validator.validateInt(disc[0])
        discGrades = disc[1]
        discipline = self.getDisciplineByID(discID, disciplineList)
        for i in range(0, len(discGrades)):
            discGrades[i] = Validator.validateInt(discGrades[i])
        discipline.addGrade(discGrades)
        return discipline
    
    def getFile(self):
        return self.__discRepo.getFile()
    
    def getDiscByID(self, ID):
        return self.__discRepo.getDiscByID(ID)
    
    def displayDisciplines(self):
        return self.__discRepo.displayDisciplines()
    
    def addDiscipline(self, disciplineName, teacherName, disciplineID = -1):
        self.__discRepo.addDiscipline(disciplineName, teacherName, disciplineID)