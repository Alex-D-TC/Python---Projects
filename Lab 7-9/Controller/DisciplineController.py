'''
Created on Nov 8, 2015

@author: AlexandruD
'''
from Utils.Utilities import Validator
from Domain.Discipline import Discipline

class DisciplineController(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def toDiscipline(self, disciplineList):
        discId = Validator.validateInt(disciplineList[0])
        discName = disciplineList[1]
        discProf = disciplineList[2]
        discipline = Discipline(discName, discProf)
        discipline.setID(discId)
        return discipline
    
    def toDisciplineByID(self, disc, disciplineList):
        discID = Validator.validateInt(disc[0])
        discGrades = disc[1]
        discipline = self.getDisciplineByID(discID, disciplineList)
        for i in range(0, len(discGrades)):
            discGrades[i] = Validator.validateInt(discGrades[i])
        discipline.addGrade(discGrades)
        return discipline
    
    def getDisciplineByID(self, ID, disciplineList):
        for discipline in disciplineList:
            if(discipline.getID() == ID): return discipline
        raise ValueError('Discipline not found')
    
    def displayDisciplines(self, disciplineList):
        disciplineArray = []
        for discipline in disciplineList:
            disciplineArray.append(discipline.displayDiscipline())
        return disciplineArray