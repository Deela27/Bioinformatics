def fibonacci(n):
    old=1
    new= 1
    for itr in range(n-1):
        tmpVal=new
        new=old
        old= tmpVal + old
    return new 

    

print(fibonacci(3))

#take first number and add it to 1
#take sum result and add to second number