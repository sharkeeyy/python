import keyboard

def is_simple_number(x) :
    divisor = 2
    while divisor < x :
        if x % divisor == 0 :
            return False
        divisor += 1
    return True

def factorize(x) :
    divisor = 2
    while x > 1 :
        if x % divisor == 0 :
            print(divisor)
            x //= divisor
        else : 
            divisor += 1    

def factorial(x):
    if x == 1 :
        return 1
    else :
        return x * factorial(x-1)
    
while True :
    x = int(input())
    print(factorial(x))  
   
