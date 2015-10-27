'''
Created on Oct 14, 2015

@author: Alex
'''
from Main_Package.validator.Validation_Tools import Validator
from Main_Package.utils.Integer_Methods import isPrime
from Main_Package.domain.globals import Sequence_Store
from math import gcd
from copy import deepcopy

class Sequence_Handler():
    
    def __init__(self):
        self.Sequence_Store = Sequence_Store()

    def display_sequence(self):
        return self.Sequence_Store.sequence
    
    def insert_at_index(self, n, index = None):
        """
            Inserts an element at a given index.
            If the index is left on it's default value(-1), then the element is simply appended
            
            Returns:
                - The original sequence, if the indexes fail validation
                - The modified sequence
        """
        if(index == None): index = len(self.Sequence_Store.sequence)
        Validator.validate_index(self.Sequence_Store.sequence, index)
        self.save_sequence()
        self.Sequence_Store.sequence.insert(index, n)
        return self.Sequence_Store.sequence
            
    def delete_from_index(self, index = -1):
        """
            Removes the element from a given index
        """
        Validator.validate_index(self.Sequence_Store.sequence, index)
        self.save_sequence()
        self.Sequence_Store.sequence.pop(index)
        return self.Sequence_Store.sequence
        # Another possible solution: return sequence[0:index] + sequence[index + 1: len(sequence)]
    
    def delete_subsequence(self, index_start, index_end):
        """
            Removes the subsequence contained within the given indexes
            Fails if the indexes are invalid
        """
        Validator.validate_index(self.Sequence_Store.sequence, index_start, index_end)
        self.save_sequence()
        i = index_end - index_start + 1
        while(i > 0):
            sequence = self.delete_from_index(index_start)
            i = i - 1
        return sequence
    
    def is_sub_sequence(self, target, index):
        for i in range(0, len(target)):
            if(i + index > len(self.Sequence_Store.sequence) - 1): 
                return -1
            if(self.Sequence_Store.sequence[i + index] != target[i]):
                return -1
        return i
    
    def fetch_index(self, target, start_index):
        """
            Returns a list containing the starting index of all the subsequences matching the target subsequence
        """
        indexList = []
        i = start_index
        while(i < len(self.Sequence_Store.sequence)):
            result = self.is_sub_sequence(target, i)
            if(result != -1):
                indexList.append(i)
                if(i + result < len(self.Sequence_Store.sequence)):
                    i += result
            i += 1
        return indexList
    
    def replace_sequence(self, target, value):
        """
            Replaces all the subsequences equal with the target subsequence with the given value subsequence
        """
        indexList = self.fetch_index(target, 0)
        if(len(indexList) != 0): 
            self.save_sequence()
        else:
            raise ValueError('Sequence not found')
        for j in range(0, len(indexList)):
            count = 0
            for i in range(indexList[j], indexList[j] + len(value)):    # We insert the subsequences at the given indexes
                sequence = self.insert_at_index(value[count], i)
                count += 1
            sequence = self.delete_subsequence(indexList[j] + count, indexList[j] + len(target) - 1 + count) # We delete the specified subsequences
            for i in range(j, len(indexList)):
                indexList[i] -= len(target) - len(value)    # We offset the rest of the indexes, relative to the new sequence
        return sequence
        
    def display_prime(self, index_start = -1, index_end = -1):
        """
            Prints a list containing all prime numbers in the given subsequence
        """
        
        result_list = []
        Validator.validate_index(self.Sequence_Store.sequence, index_start, index_end)
        for i in range(index_start, index_end + 1):
            if(isPrime(self.Sequence_Store.sequence[i])):
                result_list.append(self.Sequence_Store.sequence[i])
        return result_list
    
    def display_even(self, index_start = -1, index_end = -1):
        """
            Prints a list containing all the even numbers in the given subsequence
        """
        
        result_list = []
        Validator.validate_index(self.Sequence_Store.sequence, index_start, index_end)
        for i in range(index_start, index_end + 1):
            if(self.Sequence_Store.sequence[i] % 2 == 0):
                result_list.append(self.Sequence_Store.sequence[i])
        return result_list
    
    def sum_subsequence(self, index_start = 0, index_end = -1):
        """
            Prints the sum of all the numbers in the given subsequence
        """
        
        result = 0
        Validator.validate_index(self.Sequence_Store.sequence, index_start, index_end)
        for i in range(index_start, index_end + 1):
            result += self.Sequence_Store.sequence[i]
        return result
    
    def gcd_subsequence(self, index_start = 0, index_end = -1):
        """
            Prints the GCD of all the elements in a the given subsequence
        """
        
        result = 0
        Validator.validate_index(self.Sequence_Store.sequence, index_start, index_end)
        for i in range(index_start, index_end):
            result = gcd(self.Sequence_Store.sequence[i], self.Sequence_Store.sequence[i+1])
        return result
    
    def max_subsequence(self, index_start = 0, index_end = -1):
        """
            Prints the greatest element in a given subsequence
        """
        
        Validator.validate_index(self.Sequence_Store.sequence, index_start, index_end)
        result = self.Sequence_Store.sequence[index_start]
        for i in range(index_start + 1, index_end + 1):
            if(self.Sequence_Store.sequence[i] > result):
                result = self.Sequence_Store.sequence[i]
        return result
    
    def display_sorted_reverse(self):
        """
            Prints a sorted version of the given sequence
            The sequence is sorted in a descending order
        """
        
        temp_sequence = deepcopy(self.Sequence_Store.sequence)
        
        for i in range(0, len(temp_sequence) - 1):
            for j in range(i, len(temp_sequence)):
                if(temp_sequence[i] < temp_sequence[j]):
                    aux = temp_sequence[i]
                    temp_sequence[i] = temp_sequence[j]
                    temp_sequence[j] = aux
                    
        return temp_sequence
        
    def filter_prime(self):
        """
            Eliminates all numbers that are not prime from the sequence
        """
        result_sequence = []
        for i in range(0, len(self.Sequence_Store.sequence)):
            if(isPrime(self.Sequence_Store.sequence[i])):
                result_sequence.append(self.Sequence_Store.sequence[i])
        if(len(result_sequence) != len(self.Sequence_Store.sequence)):
            self.save_sequence()
            self.Sequence_Store.sequence = deepcopy(result_sequence)
        return result_sequence
    
    def filter_negative(self):
        """
            Eliminates all numbers that are not negative from the sequence
        """
        result_sequence = []
        for i in range(0, len(self.Sequence_Store.sequence)):
            if(self.Sequence_Store.sequence[i] < 0):
                result_sequence.append(self.Sequence_Store.sequence[i])
        if(len(result_sequence) != len(self.Sequence_Store.sequence)):
            self.save_sequence()
            self.Sequence_Store.sequence = deepcopy(result_sequence)
        return result_sequence
    
    def save_sequence(self):
        """
            Saves the subsequence if the noCopy flag has not been triggered
        """
        self.Sequence_Store.LSO_sequence.append(deepcopy(self.Sequence_Store.sequence))
    
    def undo(self):
        """
            Reverses the effect of the last operation that had an effect on the given sequence
        """
        
        #if(len(self.Sequence_Store.LSO_sequence) - 1 < 0 or self.Sequence_Store.LSO_sequence[len(self.Sequence_Store.LSO_sequence) - 1] == self.Sequence_Store.sequence):
        #    raise ValueError('Undo is unnecessary')
        self.Sequence_Store.sequence = deepcopy(self.Sequence_Store.LSO_sequence[len(self.Sequence_Store.LSO_sequence) - 1])
        self.Sequence_Store.LSO_sequence = self.Sequence_Store.LSO_sequence[:len(self.Sequence_Store.LSO_sequence) - 1]
        return self.Sequence_Store.sequence