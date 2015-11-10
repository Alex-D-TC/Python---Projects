'''
Created on Nov 8, 2015

@author: AlexandruD
'''
class IdHandler(object):
    '''
    classdocs
    '''

    @staticmethod
    def getStudID(studRepo):
        id = -1
        if(studRepo == []): 
            return 0
        for stud in studRepo:
            if(stud.getID() > id):
                id = stud.getID()
        return id + 1
    
    @staticmethod
    def getDiscID(discRepo):     
        id = -1
        if(discRepo == []):
            return 0
        for disc in discRepo:
            if(disc.getID() > id):
                id = disc.getID()
        return id + 1
    
class Validator():
    
    @staticmethod
    def validateInt(num):
        try: num = int(num)
        except ValueError:
            raise ValueError('The number is invalid')
        return num
    
class FileOperationHandler(object):
    """
    """
    def __init__(self, file = None):
        self.__file = file
    
    def setFile(self, file):
        self.__file = file
    
    def _fetchStudent(self):
        studLine = self.__fetchLine()
        if(studLine == ['']): return studLine
        if(len(studLine) <= 2):
            studDiscCount = 0
        else:
            studDiscCount = Validator.validateInt(studLine.pop(2))
        while(studDiscCount > 0):
            studLine.append(self.__fetchDisciplineStud())
            studDiscCount -= 1
        return studLine
            
    def fetchStudents(self):
        studentList = []
        student = self._fetchStudent()
        while(student != ['']):
            studentList.append(student)
            student = self._fetchStudent()
        return studentList
            
    def __fetchDiscipline(self):
        studLine = self.__fetchLine()
        return studLine
    
    def __fetchDisciplineStud(self):
        studLine = self.__fetchLine()
        try: discGradeCount = Validator.validateInt(studLine.pop(1))
        except ValueError: return ['']
        if(discGradeCount > 0):
            studLine.append(self.__fetchLine())
        else: studLine.append([])
        return studLine
    
    def fetchDisciplines(self):
        disciplineList = []
        discipline = self.__fetchDiscipline()
        while(discipline != ['']):
            disciplineList.append(discipline)
            discipline = self.__fetchDiscipline()
        return disciplineList
    
    def __fetchLine(self):
        line = self.__file.readline()
        line = line.split(sep = '\n')
        return line[0].split(sep = '-')
    
    def __fetchGrade(self):
        line = self._fetchLine()
        for i in range(0, len(line)):
            line[i] = Validator.validate_int(line[i])
        return line
        
class RepoSearcher():
    
    @staticmethod
    def searchRepo(target, repo):
        for object in repo:
            if(target == repo):
                return False
        return True