def isPrime(prim):
    "Checks if the number is prime"
    if(prim == 1):
        return "No";
    if(prim % 2 == 0 and prim != 2):
        return "No";
    for div in range(3 , prim / 2):
        if(prim % div == 0):
            return "No";
    return "Yes";
prim = int(input("Input number "))
print(isPrime(prim))
