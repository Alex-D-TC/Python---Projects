'''
Created on Nov 8, 2015

@author: AlexandruD
'''
from Utils.Utilities import Validator
from Repository.GeneralRepository import GeneralRepository
from Controller.MainController import MainController

class Menu(object):
    '''
    classdocs
    '''

    def displayMenu(self):
        print("""Menu:
  1: Add student / discipline
  4: Display students
  5: Display disciplines""")
    
    def __init__(self):
        '''
        Constructor
        '''
        self.__mainController = MainController()
        self.__generalRepository = GeneralRepository()
        
    def runMenu(self):
        command = 1
        while(command != 0):
            self.displayMenu()
            try: command = Validator.validateInt(input("Insert your command: "))
            except ValueError as e:
                print(e.args[0])
                command = -1
                continue
            
        