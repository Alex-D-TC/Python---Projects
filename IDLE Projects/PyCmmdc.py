def cmmdc(a , b):
    while(a != b):
        if(a > b):
            a = a - b
        else :
            b = b - a
    return b;

a = int(input("Insert the first number: "))
b = int(input("Insert the second number: "))
print(cmmdc(a,b))
    
    
