# args-> when the function parameter start with a asterik , it allows for number of arguments and fucntion takes them in tuple of value

def demoFunction(*args):
    print(args)

x = demoFunction(10,20,40,50,30)
print(x)