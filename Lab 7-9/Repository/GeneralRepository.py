'''
Created on Nov 8, 2015

@author: AlexandruD
'''
from Utils.Utilities import FileOperationHandler

class GeneralRepository(object):
    '''
    classdocs
    '''


    def __init__(self, gC):
        '''
        Constructor
        '''
        self.__discFile = open('Disciplines.txt')
        self.__studFile = open('Students.txt')
        self.__fileOperator = FileOperationHandler()
        self.__fileOperator.setFile(self.__discFile)
        self.__discList = self.__fileOperator.fetchDisciplines()
        for i in range(0, len(self.__discList)):
            self.__discList[i] = gC.toDiscipline(self.__discList[i])
        self.__fileOperator.setFile(self.__studFile)
        self.__studList = self.__fileOperator.fetchStudents()
        for i in range(0, len(self.__studList)):
            self.__studList[i] = gC.toStudent(self.__studList[i], self.__discList)