def isPrime(prim):
    "Checks if the number is prime"
    if(prim == 1):
        return False;
    if(prim % 2 == 0 and prim != 2):
        return False;
    for div in range(3 , int(prim / 2)):
        if(prim % div == 0):
            return False;
    return True;

def getNum(n):
    if(n == 1): return 1;
    s = 1
    while(n > 0):
        s = s + 1 ; n = n - 1
        if(not isPrime(s)):
            temp = s
            while(temp > 1):
                div = 2
                while(temp % div == 0):
                    temp /= div
                    n = n - 1
                if(n <= 0): return div
                div = div + 1
    return s

n = int(input("Input the number "))
print(getNum(n))
        
