# map() applies a given function to each element of an iterable and return an iterator containing the result.

def square(nums):
    return nums**2

numbers = [2,3,4,5,6,7,8]
testresult= list(map(square,numbers))
print(testresult)
