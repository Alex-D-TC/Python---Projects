from Main_Package import menu
from Main_Package import sequence_analyzer
from Main_Package import validation_tools

def menu_test():
    return True

def validation_test():
    assert(validation_tools.validate_int("Select your input... ", 5) == 5)
    assert(validation_tools.validate_int("Select your input... ", "asda") == -1)
    assert(validation_tools.validate_int("Select your input... ", 100001) == -1)
    assert(validation_tools.validate_int("Select your input... ", -1) == -1)
    assert(validation_tools.validate_int("Select your input... ", 2.3) == -1)
    return True

def sequence_analyzer_test():
    return True

assert(menu_test() == True)
assert(validation_test() == True)
assert(sequence_analyzer_test() == True)