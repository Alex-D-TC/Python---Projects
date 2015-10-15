'''
Created on Oct 14, 2015

@author: Alex
'''
from Main_Package.Validation_Tools import *

def insert_at_index(sequence, n, index = -1):
    while(index == None):
        index = validate_int("Specify the index ", 0, len(sequence) - 1)
    if(index == -1):
        sequence.append(n)
    else:
        sequence.insert(index, n)
    return sequence
        
def delete_from_index(sequence, index = None):
    while(index == None):
        index = validate_int("Specify the index ", 0, len(sequence) - 1)
    for i in range(index, len(sequence) - 1):
        sequence[i] = sequence[i + 1]
    return sequence[:len(sequence) - 1]
        
def delete_subsequence(sequence, index_start = None, index_end = None):
    while(index_start == None or index_start < 0 or index_start > len(sequence) or index_start > index_end):
        print("Starting index invalid, please re-enter")
        index_start = validate_int("Insert the starting index ", 0, len(sequence) - 1)
    while(index_end == None or index_end < index_start or index_end > len(sequence)):
        print("Ending index invalid, please re-enter")
        index_end = validate_int("Insert the end index ", 0, len(sequence) - 1)
    i = index_end - index_start + 1
    while(i > 0):
        sequence = delete_from_index(sequence, index_start)
        i = i - 1
    return sequence
        
def fetch_subsequence(sequence, target, start_index):
    indexList = []
    for i in range(start_index, len(sequence)):
        haveFound = True
        if(sequence[i] == target[0]):
            indexList[0] = i
            for j in range(1, len(target)):
                if(sequence[i + j] != target[j]):
                    haveFound = False
        if(haveFound == True):
            indexList[1] = i + len(target) - 1
            return indexList
    return None

def replace_sequence(sequence, target, value):
    indexList = fetch_subsequence(sequence, target, 0)
    while(indexList != None):
        count = 0
        for i in range(indexList[0], indexList[0] + len(target)):
            sequence = insert_at_index(sequence, target[count], i)
            count += 1
        sequence = delete_subsequence(sequence, indexList[0] + count, indexList[1] + count)
    return sequence
    
    