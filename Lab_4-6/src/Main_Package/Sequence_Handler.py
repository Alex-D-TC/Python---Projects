'''
Created on Oct 14, 2015

@author: Alex
'''
from Main_Package.Validation_Tools import validate_index
from Main_Package.Integer_Methods import isPrime
from Main_Package import config
from math import gcd
from copy import deepcopy

def save_sequence(sequence):
    if(not config.noCopy): 
        config.LSO_sequence.append(deepcopy(sequence))
        config.noCopy = True

def insert_at_index(sequence, n, index = -1):
    if(index == -1): index = len(sequence)
    if (not validate_index(sequence, index)):
        print('Invalid index')
        return sequence
    save_sequence(sequence)
    if(index == -1):
        sequence.append(n)
    else:
        sequence.insert(index, n)
    return sequence
        
def delete_from_index(sequence, index = -1):
    if (not validate_index(sequence, index)):
        print('Invalid index')
        return sequence
    save_sequence(sequence)
    for i in range(index, len(sequence) - 1):
        sequence[i] = sequence[i + 1]
    return sequence[:len(sequence) - 1]

def delete_subsequence(sequence, index_start, index_end):
    if (not validate_index(sequence, index_start, index_end)):
        print('Invalid index')
        return sequence
    save_sequence(sequence)
    i = index_end - index_start + 1
    while(i > 0):
        sequence = delete_from_index(sequence, index_start)
        i = i - 1
    return sequence
        
def fetch_index(sequence, target, start_index):
    indexList = []
    i = start_index
    while(i < len(sequence)):
        if(sequence[i] == target[0]):
            haveFound = True
            for j in range(1, len(target)):
                if(i + j > len(sequence) - 1): 
                    haveFound = False ; break
                if(sequence[i + j] != target[j]):
                    haveFound = False ; break
            if(haveFound == True):
                indexList.append(i)
            try: i = i + j
            except: pass
        i += 1
    return indexList

def replace_sequence(sequence, target, value):
    indexList = fetch_index(sequence, target, 0)
    if(len(indexList) != 0): 
        save_sequence(sequence)
    for j in range(0, len(indexList)):
        count = 0
        for i in range(indexList[j], indexList[j] + len(value)):
            sequence = insert_at_index(sequence, value[count], i)
            count += 1
        sequence = delete_subsequence(sequence, indexList[j] + count, indexList[j] + len(target) - 1 + count)
        for i in range(j, len(indexList)):
            indexList[i] -= len(target) - len(value)
    return sequence
    
def display_prime(sequence, index_start = 0, index_end = -1):
    result_list = []
    if(not validate_index(sequence, index_start, index_end)):
        print('Indexes are invalid...')
        return sequence
    for i in range(index_start, index_end + 1):
        if(isPrime(sequence[i])):
            result_list.append(sequence[i])
    print(result_list)
    return sequence

def display_even(sequence, index_start = 0, index_end = -1):
    result_list = []
    if(not validate_index(sequence, index_start, index_end)):
        print('Indexes are invalid...')
        return sequence
    for i in range(index_start, index_end + 1):
        if(sequence[i] % 2 == 0):
            result_list.append(sequence[i])
    print(result_list)
    return sequence

def sum_subsequence(sequence, index_start = 0, index_end = -1):
    result = 0
    if(not validate_index(sequence, index_start, index_end)):
        print('Indexes are invalid...')
        return sequence
    for i in range(index_start, index_end + 1):
        result += sequence[i]
    print(result)
    return sequence

def gcd_subsequence(sequence, index_start = 0, index_end = -1):
    result = 0
    if(not validate_index(sequence, index_start, index_end)):
        print('Indexes are invalid...')
        return sequence
    for i in range(index_start, index_end):
        result = gcd(sequence[i], sequence[i+1])
    print(result)
    return sequence

def max_subsequence(sequence, index_start = 0, index_end = -1):
    if(not validate_index(sequence, index_start, index_end)):
        print('Indexes are invalid...')
        return sequence
    result = sequence[index_start]
    for i in range(index_start + 1, index_end + 1):
        if(sequence[i] > result):
            result = sequence[i]
    print(result)
    return sequence

def display_sorted_reverse(sequence):
    temp_sequence = deepcopy(sequence)
    for i in range(0, len(temp_sequence) - 1):
        for j in range(i, len(temp_sequence)):
            if(temp_sequence[i] < temp_sequence[j]):
                aux = temp_sequence[i]
                temp_sequence[i] = temp_sequence[j]
                temp_sequence[j] = aux
    print(temp_sequence)
    
def filter_prime(sequence):
    result_sequence = []
    save_sequence(sequence)
    for i in range(0, len(sequence)):
        if(isPrime(sequence[i])):
            result_sequence.append(sequence[i])
    if(len(result_sequence) != len(sequence)):
        save_sequence(sequence)
    return result_sequence

def filter_negative(sequence):
    result_sequence = []
    for i in range(0, len(sequence)):
        if(sequence[i] < 0):
            result_sequence.append(sequence[i])
    if(len(result_sequence) != len(sequence)):
        save_sequence(sequence)
    return result_sequence

def undo(sequence):
    if(config.LSO_sequence[len(config.LSO_sequence) - 1] == sequence):
        print('Undo is unnecessary')
        return sequence
    temp_sequence = deepcopy(config.LSO_sequence[len(config.LSO_sequence) - 1])
    config.LSO_sequence = config.LSO_sequence[:len(config.LSO_sequence) - 1]
    return temp_sequence