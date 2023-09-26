#Determines fibonacci number of the nth term in the sequence.
def fibonacci(n):
    old=1
    new= 1
    for itr in range(n-1):
        tmpVal=new
        new=old
        old= tmpVal + old
    return new 

print(fibonacci(3))
