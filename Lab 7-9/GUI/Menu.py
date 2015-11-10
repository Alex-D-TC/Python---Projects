'''
Created on Nov 8, 2015

@author: AlexandruD
'''
from Utils.Utilities import Validator

class Menu(object):
    '''
    classdocs
    '''

    def displayMenu(self):
        print("""Menu:
  1: Add student / discipline
  4: Display students
  5: Display disciplines""")
    
    def __init__(self, studentController, disciplineController):
        '''
        Constructor
        '''
        self.__studentController = studentController
        self.__disciplineController = disciplineController
        self.__princCommandDictionary = {1: self.addItem,
                                         4: self.displayStudents,
                                         5: self.displayDisciplines}   
             
    def runMenu(self):
        command = 1
        while(command != 0):
            self.displayMenu()
            try: command = Validator.validateInt(input("Insert your command: "))
            except ValueError as e:
                print(e.args[0])
                continue
            #try:
            f = self.__princCommandDictionary[command]
            rez = f()
            #except Exception as e:
            #    print(e)
            
    def addItem(self):
        command = 0
        while(command > 2 or command < 1):
            print(''' Select item type to add:
   1: Student
   2: Discipline''')
            try:
                command = Validator.validateInt(input('Select your option: '))
            except ValueError:
                print('Invalid input')
        if(command == 1):
            studentName = input("Insert student name: ")
            self.__studentController.addStudent(studentName)
        else:
            disciplineName = input("Insert discipline name: ")
            teacherName = input("Insert teacher name: ")
            self.__disciplineController.addDiscipline(disciplineName, teacherName)
        
    def displayStudents(self):
        print("")
        studentArray = self.__studentController.displayStudents()
        for student in studentArray:
            for line in student:
                print(line)
    
    def displayDisciplines(self):
        print("")
        disciplineArray = self.__disciplineController.displayDisciplines()       
        for discipline in disciplineArray:
            print(discipline)
    