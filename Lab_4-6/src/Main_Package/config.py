from Main_Package.Sequence_Handler import insert_at_index, delete_from_index, delete_subsequence, replace_sequence
    
sequence = []        
LSO_sequence = []   
menu_dictionary = {
                    'add': insert_at_index,
                    'delete index': delete_from_index,
                    'delete subsequence': delete_subsequence,
                    'replace subsequence': replace_sequence,
                    'display': lambda sequence: print(sequence),
                    'quit' : lambda sequence: print('Quitting...')
                    }