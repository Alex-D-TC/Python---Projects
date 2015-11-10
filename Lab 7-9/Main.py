'''
Created on Nov 8, 2015

@author: AlexandruD
'''
from GUI.Menu import Menu
from Utils.Builder import Builder

if __name__ == '__main__':
    builder = Builder()
    menu = builder.getMenu()
    menu.runMenu()