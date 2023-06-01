# lamdba is used to make code clean and short.
# used when there is one statement


# def square(nums):
#     return nums**2

# result= square(2)
# print(result)

a = lambda x:x**2
print(a(2))

mylist = [1,2,3,4,5,6,7,8,9]
list_even = list(filter(lambda x:x%2==0,mylist))
print(list_even)