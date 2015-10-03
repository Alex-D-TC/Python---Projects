#  Dandu-se numarul natural n, determina numerele prime p1 si p2 astfel ca
# n = p1 + p2 (verificarea ipotezei lui Goldbach).

def isPrime(n):
    "Checks if the number is prime"
    if(n == 1): return False;
    if(n != 2 and n % 2 == 0): return False;
    for div in range(3 , int(n / 2)):
        if( n % div == 0): return False;
    return True;

def getPrime(start):
    "Returns the first prime number encountered exclusively after Start"
    i = 0
    if(start % 2 == 0): start = start + 1; # Forces start to be odd
    while(i == 0):
        start = start + 2;
        if(isPrime(start)):
            i = start
    return i;

def determine(n):
    p1 = getPrime(0)
    p2 = n - p1
    while(not isPrime(p2)):
        p1 = getPrime(p1)
        p2 = n - p1
    print(p1,p2)

n = int(input("Input your number: "))
determine(n)
