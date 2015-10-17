'''
Created on Oct 14, 2015

@author: Alex
'''

from Main_Package.Sequence_Handler import display_even, display_prime, insert_at_index, delete_from_index, \
                                            delete_subsequence, replace_sequence, sum_subsequence,\
    gcd_subsequence, max_subsequence, display_sorted_reverse, filter_prime,\
    filter_negative, undo
from Main_Package.String_Methods import get_word_count
from Main_Package import config
from Main_Package.Validation_Tools import validate_int

menu_dictionary = {
                    'add': insert_at_index,
                    'delete index': delete_from_index,
                    'delete subsequence': delete_subsequence,
                    'replace subsequence': replace_sequence,
                    'display': lambda sequence: print(sequence),
                    'display prime' : display_prime,
                    'display even' : display_even,
                    'display sorted reverse' : display_sorted_reverse,
                    'sum subsequence' : sum_subsequence,
                    'gcd subsequence' : gcd_subsequence,
                    'max subsequence' : max_subsequence,
                    'filter prime' : filter_prime,
                    'filter negative' : filter_negative,
                    'undo' : undo,
                    'quit' : lambda sequence: print('Quitting...')
                    }

def get_keywords(menu_split):
    key_list = []
    key_string = ''
    for i in range(0, len(menu_split)):
        num = validate_int(menu_split[i], -10000, 10000)
        if(num == None):
            key_string += menu_split[i] + ' '
        else :
            if(key_string != ''):
                key_string = key_string[:len(key_string) - 1]
                key_list.append(key_string)
            key_string = '' 
    if(key_string != ''):
        key_string = key_string[:len(key_string) - 1]
        key_list.append(key_string)
    return key_list 
        
def get_numbers(menu_split, startIndex):
    num_array = []
    for i in range(startIndex, len(menu_split)):
        num = validate_int(menu_split[i], -10000, 10000)
        if(num == None):
            break
        num_array.append(num)
    return num_array

def process_command(sequence, menu_split):
    keystring_list = get_keywords(menu_split)
    num_list = get_numbers(menu_split, get_word_count(keystring_list[0]))
    try : f = menu_dictionary[keystring_list[0]]
    except : 
        print('Invalid command')
        return sequence
    if(len(keystring_list) >= 2 and keystring_list[1] == 'with'):
            num_list = [num_list, get_numbers(menu_split, get_word_count(keystring_list[0]) + 1 + len(num_list))]
    try : 
        temp_sequence = f(sequence, *num_list)
        config.noCopy = False
        if(temp_sequence == None):
            return sequence
        return temp_sequence
    except : 
        print('Command failed')
        return sequence
    
def display_Menu(sequence):
    menu_split = [' ']
    while(menu_split[0] != 'quit'):
        menu_code = input("Input your command: ")
        menu_split = menu_code.split(sep=" ")
        sequence = process_command(sequence, menu_split)