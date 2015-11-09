'''
Created on Nov 8, 2015

@author: AlexandruD
'''
from Domain.Discipline import Discipline
from Domain.Student import Student
from Utils.Utilities import Validator

class GestionController(object):
    '''
    classdocs
    '''
    def __init__(self): pass

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
    
    def toStudent(self, studentList, disciplineList):
        studId = Validator.validateInt(studentList[0])
        studName = studentList[1]
        student = Student(studName)
        student.setID(studId)
        for i in range(2, len(studentList)):
            discipline = self.toDisciplineByID(studentList[i], disciplineList)
            student.addDiscipline(discipline)
        return student
            
    def getDisciplineByID(self, ID, disciplineList):
        for discipline in disciplineList:
            if(discipline.getID() == ID): return discipline
        raise ValueError('Discipline not found')
    
    def getStudentByID(self, ID, studentList):
        for student in studentList:
            if(student.getID() == ID): return student
        raise ValueError('Discipline not found')