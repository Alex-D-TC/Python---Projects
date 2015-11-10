'''
Created on Nov 9, 2015

@author: AlexandruD
'''
from GUI.Menu import Menu
from Controller.StudentController import StudentController
from Repository.StudentRepository import StudentRepository
from Controller.DisciplineController import DisciplineController
from Repository.DisciplineRepository import DisciplineRepository
from Domain.Student import Student
from Domain.Discipline import Discipline
from Utils.Utilities import FileOperationHandler
from Utils.FileObjectFetcher import FileObjectFetcher

class Builder(object):
    '''
    classdocs
    '''


    def __init__(self): pass
    
    def getMenu(self):
        studentController = self.getStudentController()
        disciplineController = self.getDisciplineController()
        fileFetcher = self.getFileObjectFetcher(self.getFileOperationHandler(), studentController, disciplineController, self)
        fileFetcher.prepRepos()
        return Menu(studentController, disciplineController)
    
    def getStudentController(self):
        return StudentController(self.getStudentRepo())
    
    def getStudentRepo(self):
        return StudentRepository(self)
    
    def getDisciplineController(self):
        return DisciplineController(self.getDisciplineRepo())
    
    def getDisciplineRepo(self):
        return DisciplineRepository(self)
    
    def getStudent(self, studName, studID = -1,studRepo = []):
        return Student(studName, studID, studRepo)
    
    def getDiscipline(self, discName, discTeacher, discID, discRepo):
        return Discipline(discName, discTeacher, discID, discRepo)
    
    def getFileOperationHandler(self):
        return FileOperationHandler()
    
    def getFileObjectFetcher(self, fileOp, studCtrl, discCtrl, builder):
        return FileObjectFetcher(fileOp, studCtrl, discCtrl, builder)
        