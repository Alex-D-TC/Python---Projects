'''
Created on Oct 14, 2015

@author: Alex
'''
from Main_Package.utils.Validation_Tools import validate_index
from Main_Package.utils.Integer_Methods import isPrime
from Main_Package.domain import config
from math import gcd
from copy import deepcopy

def save_sequence(sequence):
    """
        Saves the subsequence if the noCopy flag has not been triggered
    """
    if(not config.noCopy): 
        config.LSO_sequence.append(deepcopy(sequence))
        config.noCopy = True

def insert_at_index(sequence, n, index = -1):
    """
        Inserts an element at a given index.
        If the index is left on it's default value(-1), then the element is simply appended
    """
    if(index == -1): index = len(sequence)
    if (not validate_index(sequence, index)):
        print('Invalid index')
        return sequence
    save_sequence(sequence)
    sequence.insert(index, n)
    return sequence
        
def delete_from_index(sequence, index = -1):
    """
        Removes the element from a given index
    """
    if (not validate_index(sequence, index)):
        print('Invalid index')
        return sequence
    save_sequence(sequence)
    for i in range(index, len(sequence) - 1):
        sequence[i] = sequence[i + 1]
    return sequence[:len(sequence) - 1]

def delete_subsequence(sequence, index_start, index_end):
    """
        Removes the subsequence contained within the given indexes
        Fails if the indexes are invalid
    """
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
    """
        Returns a list containing the starting index of all the subsequences matching the target subsequence
    """
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
    """
        Replaces all the subsequences equal with the target subsequence with the given value subsequence
    """
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
    """
        Prints a list containing all prime numbers in the given subsequence
    """
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
    """
        Prints a list containing all the even numbers in the given subsequence
    """
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
    """
        Prints the sum of all the numbers in the given subsequence
    """
    result = 0
    if(not validate_index(sequence, index_start, index_end)):
        print('Indexes are invalid...')
        return sequence
    for i in range(index_start, index_end + 1):
        result += sequence[i]
    print(result)
    return sequence

def gcd_subsequence(sequence, index_start = 0, index_end = -1):
    """
        Prints the GCD of all the elements in a the given subsequence
    """
    result = 0
    if(not validate_index(sequence, index_start, index_end)):
        print('Indexes are invalid...')
        return sequence
    for i in range(index_start, index_end):
        result = gcd(sequence[i], sequence[i+1])
    print(result)
    return sequence

def max_subsequence(sequence, index_start = 0, index_end = -1):
    """
        Prints the greatest element in a given subsequence
    """
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
    """
        Prints a sorted version of the given sequence
        The sequence is sorted in a descending order
    """
    temp_sequence = deepcopy(sequence)
    for i in range(0, len(temp_sequence) - 1):
        for j in range(i, len(temp_sequence)):
            if(temp_sequence[i] < temp_sequence[j]):
                aux = temp_sequence[i]
                temp_sequence[i] = temp_sequence[j]
                temp_sequence[j] = aux
    print(temp_sequence)
    
def filter_prime(sequence):
    """
        Eliminates all numbers that are not prime from the sequence
    """
    result_sequence = []
    for i in range(0, len(sequence)):
        if(isPrime(sequence[i])):
            result_sequence.append(sequence[i])
    if(len(result_sequence) != len(sequence)):
        save_sequence(sequence)
    return result_sequence

def filter_negative(sequence):
    """
        Eliminates all numbers that are not negative from the sequence
    """
    result_sequence = []
    for i in range(0, len(sequence)):
        if(sequence[i] < 0):
            result_sequence.append(sequence[i])
    if(len(result_sequence) != len(sequence)):
        save_sequence(sequence)
    return result_sequence

def undo(sequence):
    """
        Reverses the effect of the last operation that had an effect on the given sequence
    """
    if(config.LSO_sequence[len(config.LSO_sequence) - 1] == sequence):
        print('Undo is unnecessary')
        return sequence
    temp_sequence = deepcopy(config.LSO_sequence[len(config.LSO_sequence) - 1])
    config.LSO_sequence = config.LSO_sequence[:len(config.LSO_sequence) - 1]
    return temp_sequence