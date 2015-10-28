'''
Created on Oct 14, 2015

@author: Alex
'''

from Main_Package.controller.Command_Handler import Command_Handler
from Main_Package.utils.String_Methods import get_index

class GUI_Handler:
    
    def __init__(self):
        self.Command_Handler = Command_Handler()
    
    def display_Menu(self):
        """
            Displays the menu, waits for and processes commands
        """
        menu_split = [' ']
        while(menu_split[0] != 'quit'):
            menu_code = input("Input your command: ")
            menu_split = menu_code.split(sep=" ")
            try:
                sequence = self.Command_Handler.process_command(menu_split)
                print(sequence)
            except TypeError as e:
                if(get_index(e.args[0].split(sep = " "), 1) == 'takes'): print('Invalid command')
                else: print(e.args[0])
            except ValueError as e:
                print (e.args[0])
            except IndexError as e:
                print (e.args[0])