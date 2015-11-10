'''
Created on Nov 10, 2015

@author: AlexandruD
'''
from Utils.Utilities import Validator
from copy import deepcopy

class FileObjectFetcher(object):
    '''
    classdocs
    '''


    def __init__(self, fileOpHandler, studCtrl, discCtrl, builder):
        '''
        Constructor
        '''
        self.__fileOpHandler = fileOpHandler
        self.__builder = builder
        self.studCtrl = studCtrl
        self.discCtrl = discCtrl
        
    def prepRepos(self):
        self.__prepDiscRepo()
        self.__prepStudRepo()
            
    def __prepDiscRepo(self):
        self.__fileOpHandler.setFile(self.discCtrl.getFile())
        discList = self.__fileOpHandler.fetchDisciplines()
        for disc in discList:
            discID = Validator.validateInt(disc[0])
            discName = disc[1]
            discTeacher = disc[2]
            self.discCtrl.addDiscipline(discName, discTeacher, discID)

    def __prepStudRepo(self):
        self.__fileOpHandler.setFile(self.studCtrl.getFile())
        studList = self.__fileOpHandler.fetchStudents()
        for stud in studList:
            studName = stud[1]
            studID = Validator.validateInt(stud[0])
            student = self.__builder.getStudent(studName, studID)
            for i in range(2, len(stud)):
                discID = Validator.validateInt(stud[i][0])
                discGrades = stud[i][1]
                discipline = deepcopy(self.discCtrl.getDiscByID(discID))
                for grade in discGrades:
                    discipline.addGrade(Validator.validateInt(grade))
                student.addDiscipline(discipline)
            self.studCtrl.addStud(student)