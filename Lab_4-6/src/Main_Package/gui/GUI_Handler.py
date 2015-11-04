'''
Created on Oct 14, 2015

@author: Alex
'''

from Main_Package.controller.Command_Handler import Command_Handler
from Main_Package.utils.String_Methods import get_index
from Main_Package.validator.Validation_Tools import Validator

class GUI_Handler:
    
    def __init__(self):
        self.Command_Handler = Command_Handler()
    
    def _print_sequence(self, sequence, end_character):
        if(not len(sequence) == 0):
            for i in range(0, len(sequence)):
                print(sequence[i], end= end_character)
        print(" ",end = "\n")
    
    def display_Menu(self):
        """
            Displays the menu, waits for and processes commands
        """
        menu_split = [' ']
        self._print_sequence(self.Command_Handler.menu_dictionary['display menu'](None), "")
        while(menu_split[0] != 'quit'):
            menu_code = input("Input your command: ")
            menu_split = menu_code.split(sep=" ")
            try:
                sequence = self.Command_Handler.process_command(menu_split)
                if(isinstance(sequence, int)):
                    print(sequence)
                else:
                    try:
                        Validator.validate_int(get_index(sequence, 0), -10000, 10000)
                        end_character = " "
                    except IndexError:
                        pass
                    except ValueError:
                        end_character = ""
                    self._print_sequence(sequence, end_character)
            except TypeError as e:
                if(get_index(e.args[0].split(sep = " "), 1) == 'takes'): print('Invalid command')
                else: print(e.args[0])
            except ValueError as e:
                print (e.args[0])
            except IndexError as e:
                print (e.args[0])