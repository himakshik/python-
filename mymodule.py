def fact(num):
    factorial = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")  
    elif num == 0:
        print("The factorial of 0 is 1")  
    else:
        for i in range(1,num + 1):
            factorial = factorial*i  
    print("The factorial of",num,"is",factorial)
    return 


def prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                break
            else:
                print(num,"is a prime number")
    else:
        print(num,"is not a prime number")

    return 

def armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10


    if num == sum:
        print(num,"is an Armstrong number")
    else:
        print(num,"is not an Armstrong number")
    return 

def power(num,p):
    n = num**p
    print(num,"to the power",p,"is: ",n)
    return
    
