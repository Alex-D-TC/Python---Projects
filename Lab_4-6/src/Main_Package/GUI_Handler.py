'''
Created on Oct 14, 2015

@author: Alex
'''

from Main_Package.config import menu_dictionary

def process_command(sequence, menu_split):
    arg_list = ''
    count = 0
    for i in range(0, len(menu_split)):
        isDone = False
        for j in range(0, len(menu_split[i])):
            if(menu_split[i][j].isdigit()):
                isDone = True
                break
        if(isDone): break
        arg_list += menu_split[i] + ' '
        count += 1
    arg_list = arg_list[:len(arg_list) - 1]
    try: f = menu_dictionary[arg_list]
    except : 
        print('Invalid keyword')
        return sequence
    arg_list = []
    #ADD CHECK FOR 'WITH' KEYWORD
    //
    for i in range(count, len(menu_split)):
        if(not menu_split[i].isdigit()):
            print('Invalid parameters')
            return sequence
        arg_list.append(int(menu_split[i]))
    if(len(menu_split) > 1):
        try : sequence = f(sequence, *arg_list)
        except : print('Operation failed')
        return sequence
    try: f(sequence)
    except: print('Operation failed')
    return sequence

def display_Menu(sequence):
    menu_split = [' ']
    while(menu_split[0] != 'quit'):
        menu_code = input("Input your command: ")
        menu_split = menu_code.split(sep=" ")
        sequence = process_command(sequence, menu_split)
        menu_code = None