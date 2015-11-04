'''
Created on Oct 31, 2015

@author: Alex
'''

class FileStream_Retriever(object):
    '''
        Used for retrieving filestreams from files
    '''
    
    @staticmethod    
    def retrieve_text(filename):
        """
            Retrieves the text content of a file
        """
        file = open(filename)
        lineArray = []
        for line in file:
            lineArray.append(line)
        file.close()
        return lineArray
    
    @staticmethod
    def format_file_text(filename):
        lineArray = FileStream_Retriever.retrieve_text(filename)
        for i in range(0, len(lineArray)):
            lineArray[i] = bytes(lineArray[i],'utf-8').decode('unicode_escape')
        return lineArray