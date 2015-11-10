'''
Created on Nov 9, 2015

@author: AlexandruD
'''
from Utils.Utilities import Validator

class StudentRepository(object):
    '''
    classdocs
    '''


    def __init__(self, builder):
        '''
        Constructor
        '''
        self.__file = open('Students.txt')
        self.__builder = builder
        self.__studentList = []
    
    def getStudentByID(self, ID, studentList):
        for student in studentList:
            if(student.getID() == ID): return student
        raise ValueError('Discipline not found')
        
    def getStudents(self):
        return self.__studentList
    
    def displayStudents(self):
        studentArray = []
        if(self.__studentList == studentArray):
            return studentArray
        for student in self.__studentList:
            studentArray.append(student.displayStudent())
        return studentArray
    
    def addStudent(self, studentName, studID):
        student = self.__builder.getStudent(studentName, studID, self.__studentList)
        self.__studentList.append(student)
        
    def addStudents(self, students):
        for student in students:
            self.__studentList.append(student)
            
    def getFile(self):
        return self.__file