'''
Created on Nov 8, 2015

@author: AlexandruD
'''
from Utils.Utilities import Validator
from Domain.Student import Student

class StudentController(object):
    '''
    classdocs
    '''


    def __init__(self, toDiscFunction):
        '''
        Constructor
        '''
        self.toDisciplineByID = toDiscFunction
        
    def toStudent(self, studentList, disciplineList):
        studId = Validator.validateInt(studentList[0])
        studName = studentList[1]
        student = Student(studName)
        student.setID(studId)
        for i in range(2, len(studentList)):
            discipline = self.toDisciplineByID(studentList[i], disciplineList)
            student.addDiscipline(discipline)
        return student
    
    def getStudentByID(self, ID, studentList):
        for student in studentList:
            if(student.getID() == ID): return student
        raise ValueError('Discipline not found')
    
    def addStudent(self, studentName, studRepo):
        student = Student(studentName, studRepo)
        studRepo.append(student)
        
    def displayStudents(self, studentList):
        studentArray = []
        for student in studentList:
            studentArray.append(student.displayStudent())
        return studentArray