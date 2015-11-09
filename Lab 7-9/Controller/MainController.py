'''
Created on Nov 8, 2015

@author: AlexandruD
'''
from Controller.GestionController import GestionController
from Controller.CRUDController import CRUDController 

class MainController(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__gestionController = GestionController()
        self.__crudController = CRUDController()