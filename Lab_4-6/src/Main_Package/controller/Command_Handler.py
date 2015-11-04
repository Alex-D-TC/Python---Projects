'''
Created on Oct 23, 2015

@author: Alex
'''

from Main_Package.repository.Sequence_Handler import Sequence_Handler
from Main_Package.utils.String_Methods import get_word_count, get_index
from Main_Package.validator.Validation_Tools import Validator
from Main_Package.utils.FileStream_Retriever import FileStream_Retriever

class Command_Handler:
    """
        Handles the parsing of commands.
    """
    def __init__(self):
        """
            The constructor
        """
        self.sequence_handler = Sequence_Handler()
        self.menu_dictionary = {                  # A dictionary containing all the available commands and their assigned function
                            'add': Sequence_Handler.insert_at_index,
                            'delete index': Sequence_Handler.delete_from_index,
                            'delete subsequence': Sequence_Handler.delete_subsequence,
                            'replace subsequence': Sequence_Handler.replace_sequence,
                            'display' : Sequence_Handler.display_sequence,
                            'display menu': lambda temp: FileStream_Retriever.retrieve_text('Readme.txt'),
                            'display prime' : Sequence_Handler.display_prime,
                            'display even' : Sequence_Handler.display_even,
                            'display sorted reverse' : Sequence_Handler.display_sorted_reverse,
                            'sum subsequence' : Sequence_Handler.sum_subsequence,
                            'gcd subsequence' : Sequence_Handler.gcd_subsequence,
                            'max subsequence' : Sequence_Handler.max_subsequence,
                            'filter prime' : Sequence_Handler.filter_prime,
                            'filter negative' : Sequence_Handler.filter_negative,
                            'undo' : Sequence_Handler.undo,
                            'redo' : Sequence_Handler.redo,
                            'quit' : lambda temp: 'Quitting...'
                            }
    
    def get_keywords(self, menu_split):
        """
            Gets all the keystrings of a given command
            Example: 
                    - "replace subsequence 1 3 5 with 4 5" will return ["replace subsequence", "with"]
                    - "delete index 1" will return ["delete index"]
                    
            Input:
                -menu_split - The command string
            
            Returns:
                An array containing all identified keystrings
        """
        key_list = []
        key_string = ''
        for i in range(0, len(menu_split)):
            try: 
                num = Validator.validate_int(get_index(menu_split,i), -10000, 10000)
                if(key_string != ''):
                    key_string = key_string[:len(key_string) - 1]
                    key_list.append(key_string)
                key_string = ''  
            except ValueError as e:
                if(get_index(e.args, 0) == "Number is invalid"):
                    key_string += get_index(menu_split,i) + ' '
        if(key_string != ''):
            key_string = key_string[:len(key_string) - 1]
            key_list.append(key_string)
        return key_list 
            
    def get_numbers(self, menu_split, startIndex):
        """
            Gets the first array of numbers encountered after a given index
            
            Input:
                -menu_split - The command string, split into an array of strings by the ' ' character
                -sequence - The base sequences
                
            Returns:
                The first array of numbers encountered
        """
        num_array = []
        for i in range(startIndex, len(menu_split)):
            try: num = Validator.validate_int(menu_split[i], -10000, 10000)
            except ValueError:
                break
            num_array.append(num)
        return num_array
    
    def process_command(self, menu_split):
        """
            Process a given command in order to determine the called function and it's parameters
            If the command is valid, the function is called
            
            Input: 
                -menu_split - The command string, split into an array of strings by the ' ' character
                -sequence - The base sequence
                
            Returns:
                The sequence, modified by the function called by the command string if the command is executed successfully
                The unmodified sequence, if the command string is invalid, or the function call fails
        """
        keystring_list = self.get_keywords(menu_split)
        num_list = self.get_numbers(menu_split, get_word_count(keystring_list[0]))
        try : f = self.menu_dictionary[get_index(keystring_list, 0)]
        except : 
            raise ValueError("Invalid command")
        if(len(keystring_list) == 2 and get_index(keystring_list, 1) != 'with'):  # If we find the keyword with, we have a command of the form [ keystring number_list with numbar_list ]     
            raise ValueError('Invalid input')
        elif(len(keystring_list) == 2):    
            num_list = [num_list, self.get_numbers(menu_split, get_word_count(get_index(keystring_list, 0)) + 1 + len(num_list))] # the list num_list becomes an array of two number lists
        temp_sequence = f(self.sequence_handler, *num_list)
        return temp_sequence