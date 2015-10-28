'''
Created on Oct 14, 2015

@author: Alex
'''

class Validator():
    
    @staticmethod
    def validate_int(n, min, max):
        """
            Checks if the given input is valid, and within the specified range
            
            Input:
                - n - The given number, passed as a string
                - min - The minimum available value
                - max - The maximum available value
                
            Returns:
                - None if the number is invalid
                - The number, converted to int, if it's valid
        """
        try: n = int(n)
        except : 
            raise ValueError("Number is invalid")
        if(n < min or n > max):
            raise ValueError("Number is outside of the given range")
        return n
    
    @staticmethod
    def validate_index(sequence, index_start, index_end = -1):
        """
            Checks if the given indexes are valid.
            Fails if:
                    - index_start < 0 or index_start > index_end
                    - index_end > the length of the sequence
                    
            Input:
                - sequence - The given sequence
                - index_start - The starting index
                - intex_end - The ending index
        """
        if(index_end == -1): index_end = len(sequence)
        if(index_start > index_end or index_start < 0 or index_end > len(sequence)):
            raise IndexError('Invalid index...')
