# Required problems: P 13 - 16



class validation_tools():
    
    @staticmethod
    def validate_int(input_text, n = 0):
        """ Validates integer inputs
            Returns: 
                - None if the input is invalid or out of the allowed bounds
                - The inputted number
        """
        if(n == 0): n = input(input_text)
        try: n = int(n)
        except : 
            print("Your input is invalid")
            return None
        if(n < 0 or n > 100000):
            print("Input exceeded allowed bounds")
            return None
        return n
    
    @staticmethod
    def validate_sequence_input(input_text):
        """ Validates integer inputs for sequences
            Returns:
                - None if the input is invalid or out of the allowed bounds
                - The inputted number
        """
        n = input(input_text)
        try: n = int(n)
        except:
            print("Your input is invalid")
            return None
        if(n > 100000):
            print("Input exceeded allowed bounds")
            return None
        return n

    @staticmethod
    def validate_choice(input_text, n, menu_dictionary):
        """ Validates integer inputs for menu codes
            ! To be used in conjunction with the menu class only
            Returns:
                - None if the input is invalid or out of the allowed bounds
                - The choice code used to call the functions in menu_dictionary
        """
        choice = validation_tools.validate_int(input_text)
        if(choice == -1):
            print("Invalid choice! ") 
            return choice;
        elif(choice == 2 and n == 0):
            print("No sequence inserted! Insert a sequence first")
            return None;
        if(choice > len(menu_dictionary)):
            print("Invalid choice! ")
            return None;
        return choice
    
class sequence_analyzer():

    def __init__(self):
        " Constructor "
        self.n = 0
        self.sequence = []

    def sequence_input(self):
        """ Handles the input of number sequences 
        """
        self.n = None
        while(self.n == None):
            self.n = validation_tools.validate_int("Input sequence count: ")
        if(len(self.sequence) > 0): self.sequence = []
        for i in range(0, self.n):
            input_value = None
            while(input_value == None):
                input_value = validation_tools.validate_sequence_input("Input a number of said sequence: ")
            self.sequence.append(input_value)
        print(self.sequence)
        
    def generate_vector(self, num):
        """ Generates a binary array 
            Values:
                - 1 if the given index letter has been found
                - 0 if the given index letter has not been found
        """
        v = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        while(num > 0):
            if(v[num % 10] == 0): v[num % 10] = 1;
            num //= 10
        return v
    
    def equal_vectors(self, destination, source):
        """ Checks if two arrays are equal
            Return: True or False
        """
        for i in range (0, 9):
            if(destination[i] != source[i]):
                return False
        return True

    def identify_sequence(self, index): # 
        """ Used in conjunction with prob_13 to identify the subsequence of the given property, starting from the given index
            Return: The index of the end of the subsequence, if it has been found / -1 if we have not found a substring
        """ 
        add = 0
        for i in range(index, self.n):
            if(add + self.sequence[i] >= 5):
                if(add + self.sequence[i] == 5): return i;
                return index - 1;
            add = add + self.sequence[i];
        if(add == 5):
            return self.n
        return index - 1;
            
    def prob_13(self):
        """ Problem - 13 """
        psM = 0 ; lM = 0 ; end = 0
        for i in range(0, self.n):
            end = self.identify_sequence(i) # we identify the subsequence externally
            if(end - i + 1 > lM):           # we check if we have a new max substring. If we do, we record it
                lM = end - i + 1
                psM = i
        if(lM == 0): return "No sequence found" # the minimum length must be 1
        return self.sequence[psM : psM + lM]
    
    def prob_16(self):
        """ Problem - 16 """
        pS = 0 ; l = 1 ; psM = 0 ; lM = 0 ; trans_v = self.generate_vector(self.sequence[0]) # trans_v is a "transport value", recording the binary vector to compare the rest of the
        for i in range(0, self.n - 1):                                                       # subsequence with
            if(not self.equal_vectors(trans_v, self.generate_vector(self.sequence[i + 1]))):
                if(l > lM):
                    lM = l      # we change the maximum length and the start of the greatest substring
                    psM = pS
                pS = i + 1
                l = 0
                trans_v = self.generate_vector(self.sequence[i + 1]) # if we have reached the end of our subsequence, we create the binary vector of the start of the substring
            l += 1
        if(lM == 1): return "No sequence found" # the minimum length must be 2
        return self.sequence[psM : psM + lM]
    
class menu():
    
    def __init__(self):
        " Constructor "
        self.analyzer = sequence_analyzer()
        self.menu_dictionary = {    # We create a dictionary to use in place of the switch statement
              1: self.analyzer.sequence_input,
              2: self.analyzer.prob_13,
              3: self.analyzer.prob_16,
              4: lambda : print("Quitting...")
            }
    
    
    def display_Menu(self):
        """ Displays the menu and responds to input
            Return: The choice code used to call the functions stored in menu_dicitonary
        """
        choice = None
        print("Option 1: Sequence insertion")
        print("Option 2: P 13")
        print("Option 3: P 16")
        print("Option 4: Exit")
        while(choice == None): 
            choice = validation_tools.validate_choice("Select an option: ", self.analyzer.n, self.menu_dictionary)
        return choice;

    def update_menu(self):
        """ Menu input handling """
        menu_code = -1;
        while(menu_code != 4):
            menu_code = self.display_Menu()
            if(menu_code >= 2 and menu_code <= 3): 
                print(self.menu_dictionary[menu_code]())
            self.menu_dictionary[menu_code]()
    

    