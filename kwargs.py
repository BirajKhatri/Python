# **kwargs-> it builds a dictionary of key/value pairs


def myfunction(**kwargs):
    print(kwargs)
    if 'fname' in kwargs:
        print('True')
    else:
        print('False')

myfunction(fname='Ram',lname='Shrestha')