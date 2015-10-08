# Required probs: P 13 - 16

# We instantiate a dictionary to use in place of the switch statement

class sequence_analyzer():

    def __init__(self):
        self.n = 0
        self.sequence = []
        self.menu_dictionary = {
              1: self.sequence_input,
              2: self.prob_13,
              3: self.prob_16,
              4: self.quitM
            }
        
    def quitM(self): print("Quitting...")

    def sequence_input(self):
        self.n = -1
        while(self.n == -1):
            self.n = self.validate_int(self.n, "Input sequence count: ")
        if(len(self.sequence) > 0): self.sequence = []
        for i in range(0, self.n):
            input_value = -1
            while(input_value == -1):
                input_value = self.validate_int(input_value, "Input a number of said sequence: ")
            self.sequence.append(input_value)
        print(self.sequence)
        
    def generate_vector(self, num):
        v = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        while(num > 0):
            if(v[num % 10] == 0): v[num % 10] = 1;
            num //= 10
        return v
    
    def equal_vectors(self, destination, source):
        for i in range (0, 9):
            if(destination[i] != source[i]):
                return False
        return True

    def identify_sequence(self, index):
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
        psM = 0 ; lM = 0 ; end = 0
        for i in range(0, self.n):
            end = self.identify_sequence(i)
            if(end - i + 1 > lM):
                lM = end - i + 1
                psM = i
        if(lM == 0): return "No sequence found"
        return self.sequence[psM : psM + lM]
    
    def prob_16(self):
        pS = 0 ; l = 1 ; psM = 0 ; lM = 0 ; trans_v = self.generate_vector(self.sequence[0])
        for i in range(0, self.n - 1):
            if(not self.equal_vectors(trans_v, self.generate_vector(self.sequence[i + 1]))):
                if(l > lM):
                    lM = l
                    psM = pS
                pS = i + 1
                l = 0
                trans_v = self.generate_vector(self.sequence[i + 1])
            l += 1
        if(lM == 1): return "No sequence found"
        return self.sequence[psM : psM + lM]
    
    def validate_int(self, n, input_text):
        n = input(input_text)
        try: n = int(n)
        except : 
            print("Your input is invalid")
            return -1
        return n

    def validate_choice(self, choice, input_text):
        choice = self.validate_int(choice, input_text)
        if(choice == -1): 
            return choice;
        elif(choice == 2 and self.n == 0):
            print("No sequence inserted! Insert a sequence first")
            return -1;
        if(choice > len(self.menu_dictionary)):
            print("Invalid choice! ")
            return -1;
        return choice

    def display_Menu(self):
        choice = -1
        print("Option 1: Sequence insertion")
        print("Option 2: P 13")
        print("Option 3: P 16")
        print("Option 4: Exit")
        while(choice == -1): 
            choice = self.validate_choice(choice, "Select an option: ")
        return choice;

    def main_function(self):
        menu_code = -1;
        while(menu_code != 4):
            menu_code = self.display_Menu()
            if(menu_code >= 2 and menu_code <= 3): 
                print(self.menu_dictionary[menu_code]())
            self.menu_dictionary[menu_code]()

seq = sequence_analyzer()
seq.main_function()

    

    