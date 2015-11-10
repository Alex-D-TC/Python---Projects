'''
Created on Nov 9, 2015

@author: AlexandruD
'''

class DisciplineRepository(object):
    '''
    classdocs
    '''


    def __init__(self, builder):
        '''
        Constructor
        '''
        self.__file = open('Disciplines.txt')
        self.__builder = builder
        self.__disciplineList = []
        
    def getDisciplines(self):
        return self.__disciplineList
    
    def addDiscipline(self, discName, discTeacher, discID = -1):
        discipline = self.__builder.getDiscipline(discName, discTeacher, discID, self.__disciplineList)
        self.__disciplineList.append(discipline)
        
    def addDisciplines(self, disciplines):
        for discipline in disciplines:
            self.addDiscipline(discipline)
            
    def getFile(self):
        return self.__file
    
    def getDiscByID(self, ID):
        for disc in self.__disciplineList:
            if(disc.getID() == ID):
                return disc
        raise ValueError('Discipline not existing')
    
    def displayDisciplines(self):
        discList = []
        for discipline in self.__disciplineList:
            discList.append(discipline.displayDiscipline())
        return discList