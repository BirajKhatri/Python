# function is a block of code which perform particular task when we called it. it can reuse

# to define a function
def demoFunction():
    print("welcome to kathford college")

demoFunction()


def primeChecker(x):
    for i in range(2,x//2+1):
        if(x%i==0):
            return False

    return True

print(primeChecker(2)) 

