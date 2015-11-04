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
        """
            The constructor
            Instantiates the sequence_store field
        """
        self.sequence_store = Sequence_Store()

    def display_sequence(self):
        """
            Returns the sequence, usually for display purposes
        """
        return self.sequence_store.sequence
    
    def insert_at_index(self, n, index = None, noCopy = False):
        """
            Inserts an element at a given index.
            If the index is left on it's default value(-1), then the element is simply appended
            
            Returns:
                - The original sequence, if the indexes fail validation
                - The modified sequence
            Raises IndexError if the given index is invalid
        """
        if(index == None or index == len(self.sequence_store.sequence)): index = len(self.sequence_store.sequence) # We consider this value implicitly valid
        else: Validator.validate_index(self.sequence_store.sequence, index)
        self.sequence_store.sequence.insert(index, n)
        if(not noCopy):
            self._save_sequence()
        return self.sequence_store.sequence
            
    def delete_from_index(self, index = -1, noCopy = False):
        """
           Deletes the number from a given index
           Input:
               index - The index to delete from
               noCopy - A flag used to stop the saving of the sequence
                      - Set to true when the method is called by another member method
            Returns:
                The modified sequence
            Raises IndexError if the given index is invalid
        """
        Validator.validate_index(self.sequence_store.sequence, index)
        self.sequence_store.sequence.pop(index)
        if(not noCopy):
            self._save_sequence()
        return self.sequence_store.sequence
        # Another possible solution: return sequence[0:index] + sequence[index + 1: len(sequence)]
    
    def delete_subsequence(self, index_start, index_end, noCopy = False):
        """
            Removes the subsequence contained within the given indexes
            Input:
                index_start - The starting index
                index_end - The end index
                noCopy - A flag used to stop the saving of the sequence
                      - Set to true when the method is called by another member method
            Returns:
                The modified sequence
            Raises IndexError if any of the indexes are invalid
        """
        Validator.validate_index(self.sequence_store.sequence, index_start, index_end)
        i = index_end - index_start + 1
        while(i > 0):
            sequence = self.delete_from_index(index_start, True)
            i = i - 1
        if(not noCopy):
            self._save_sequence()
        return sequence
    
    def _is_sub_sequence(self, target, index):
        """
            Finds the first occurrence of a subsequence in the sequence
            The search starts at a given index
            Input:
                target - The target subsequence
                index - The starting point of the current search
            Returns:
                The starting index of the subsequence, if it's found
                -1 if there is no subsequence
            
        """
        for i in range(0, len(target)):
            if(i + index > len(self.sequence_store.sequence) - 1): 
                return -1
            if(self.sequence_store.sequence[i + index] != target[i]):
                return -1
        return i
    
    def _fetch_index(self, target, start_index):
        """
            Returns a list containing the starting index of all the subsequences matching the target subsequence
            Input:
                target - The target subsequence
                index - The starting point of the search
            Returns:
                A list containing all found indexes
        """
        indexList = []
        i = start_index
        while(i < len(self.sequence_store.sequence)):
            result = self._is_sub_sequence(target, i)
            if(result != -1):
                indexList.append(i)
                if(i + result < len(self.sequence_store.sequence)):
                    i += result
            i += 1
        return indexList
    
    def replace_sequence(self, target, value):
        """
            Replaces all occurrences of the target subsequence with the given value subsequence
            Input:
                target - The target subsequence
                value - The replacement subsequence
            Returns:
                The modified subsequence, if it has been modified
            Raises ValueError if the target has not been found
        """
        indexList = self._fetch_index(target, 0)
        for j in range(0, len(indexList)):
            count = 0
            for i in range(indexList[j], indexList[j] + len(value)):    # We insert the subsequences at the given indexes
                sequence = self.insert_at_index(value[count], i, True)
                count += 1
            sequence = self.delete_subsequence(indexList[j] + count, indexList[j] + len(target) - 1 + count, True) # We delete the specified subsequences
            for i in range(j, len(indexList)):
                indexList[i] -= len(target) - len(value)    # We offset the rest of the indexes, relative to the new sequence
        if(len(indexList) != 0): 
            self._save_sequence()
        else:
            raise ValueError('Sequence not found')
        return sequence
        
    def display_prime(self, index_start = -1, index_end = -1):
        """
            Prints a list containing all prime numbers in the given subsequence
            Input:
                index_start - The starting index
                index_end - The ending index
            Returns:
                A list of all prime numbers between the given indexes
            Raises IndexError if any of the indexes are invalid
        """
        result_list = []
        Validator.validate_index(self.sequence_store.sequence, index_start, index_end)
        for i in range(index_start, index_end + 1):
            if(isPrime(self.sequence_store.sequence[i])):
                result_list.append(self.sequence_store.sequence[i])
        return result_list
    
    def display_even(self, index_start = -1, index_end = -1):
        """
            Prints a list containing all even numbers in the given subsequence
            Input:
                index_start - The starting index
                index_end - The ending index
            Returns:
                A list of all even numbers between the given indexes
            Raises IndexError if any of the indexes are invalid
        """
        
        result_list = []
        Validator.validate_index(self.sequence_store.sequence, index_start, index_end)
        for i in range(index_start, index_end + 1):
            if(self.sequence_store.sequence[i] % 2 == 0):
                result_list.append(self.sequence_store.sequence[i])
        return result_list
    
    def sum_subsequence(self, index_start = 0, index_end = -1):
        """
            Prints the sum of all the numbers in the given subsequence
            Input:
                index_start - The starting index
                index_end - The ending index
            Returns:
                The sum of all elements between the given indexes
            Raises IndexError if any of the indexes are invalid
        """
        
        result = 0
        Validator.validate_index(self.sequence_store.sequence, index_start, index_end)
        for i in range(index_start, index_end + 1):
            result += self.sequence_store.sequence[i]
        return result
    
    def gcd_subsequence(self, index_start = 0, index_end = -1):
        """
            Prints the gcd of all the numbers in the given subsequence
            Input:
                index_start - The starting index
                index_end - The ending index
            Returns:
                The gcd of all elements between the given indexes
            Raises IndexError if any of the indexes are invalid
        """
        
        result = 0
        Validator.validate_index(self.sequence_store.sequence, index_start, index_end)
        for i in range(index_start, index_end):
            result = gcd(self.sequence_store.sequence[i], self.sequence_store.sequence[i+1])
        return result
    
    def max_subsequence(self, index_start = 0, index_end = -1):
        """
            Prints the greatest element of all the numbers in the given subsequence
            Input:
                index_start - The starting index
                index_end - The ending index
            Returns:
                The greatest element of all elements between the given indexes
            Raises IndexError if any of the indexes are invalid
        """
        
        Validator.validate_index(self.sequence_store.sequence, index_start, index_end)
        result = self.sequence_store.sequence[index_start]
        for i in range(index_start + 1, index_end + 1):
            if(self.sequence_store.sequence[i] > result):
                result = self.sequence_store.sequence[i]
        return result
    
    def display_sorted_reverse(self):
        """
            Prints a sorted version of the given sequence
            The sequence is sorted in a descending order
            Returns:
                The index sorted in a descending order
        """
        
        temp_sequence = deepcopy(self.sequence_store.sequence)
        
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
            Returns:
                A sequence containing all prime numbers of the sequence
        """
        result_sequence = []
        for i in range(0, len(self.sequence_store.sequence)):
            if(isPrime(self.sequence_store.sequence[i])):
                result_sequence.append(self.sequence_store.sequence[i])
        if(len(result_sequence) != len(self.sequence_store.sequence)):
            self.sequence_store.sequence = deepcopy(result_sequence)
            self._save_sequence()
        return result_sequence
    
    def filter_negative(self):
        """
            Eliminates all numbers that are not negative from the sequence
            Returns:
                A sequence containing all negative numbers of the sequence
        """
        result_sequence = []
        for i in range(0, len(self.sequence_store.sequence)):
            if(self.sequence_store.sequence[i] < 0):
                result_sequence.append(self.sequence_store.sequence[i])
        if(len(result_sequence) != len(self.sequence_store.sequence)):
            self.sequence_store.sequence = deepcopy(result_sequence)
            self._save_sequence()
        return result_sequence
    
    def _save_sequence(self):
        """
            Saves the subsequence
            Used after a destructive operation
        """
        self.sequence_store.LSO_index += 1
        self.sequence_store.LSO_sequence = self.sequence_store.LSO_sequence[0:self.sequence_store.LSO_index]
        self.sequence_store.LSO_sequence.append(deepcopy(self.sequence_store.sequence))
    
    def redo(self):
        """
            Redoes an operation
        """
        self.sequence_store.LSO_index += 1
        if(self.sequence_store.LSO_index == len(self.sequence_store.LSO_sequence)):
            self.sequence_store.LSO_index -= 1
            raise IndexError('Redo is impossible')
        self.sequence_store.sequence = deepcopy(self.sequence_store.LSO_sequence[self.sequence_store.LSO_index])
        return self.sequence_store.sequence
    
    def undo(self):
        """
            Reverse the sequence a state before the last successfull distructive operation
        """
        self.sequence_store.LSO_index -= 1
        if(self.sequence_store.LSO_index < -1):
            self.sequence_store.LSO_index += 1
            raise IndexError('Undo is impossible')
        if(self.sequence_store.LSO_index == -1): 
            self.sequence_store.sequence = []
            return []
        self.sequence_store.sequence = deepcopy(self.sequence_store.LSO_sequence[self.sequence_store.LSO_index])
        #self.sequence_store.LSO_sequence = self.sequence_store.LSO_sequence[:len(self.sequence_store.LSO_sequence) - 1]
        return self.sequence_store.sequence