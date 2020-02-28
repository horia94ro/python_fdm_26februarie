def square(x):
    return x ** 2



def odd_or_even(x):
    if x % 2 == 0:
        print("EVEN")
        return
    print("ODD")


# print(square(10))
# print(square(5))
# odd_or_even(10)
# print(odd_or_even(7)) #It displays None because the function doesn't return anything


# def adding(a, b = 10, c = False):
#     if c != False:
#         return a + b + c
#     if type(a) == type(b):
#         return a + b
#     else:
#         return ("Types of a and b are not matching!")
#
# # print(adding(10, 3))
# # print(adding(12.5, 3.7))
# # print(adding("Telecom", " Academy"))
# # print(adding([1, 2, 3], [4, 5, 6]))
# # print(adding("Telecom", 13))
# # print(adding(10, 3, 3))
# # print(adding(8))
# print(adding(b = 17, c = 22, a = 33))
# print(adding(a = 20))




def calculate(x):
    square = x ** 2
    cube = x ** 3
    return square, cube


# res = calculate(25)
# print(f"The square value is: {res[0]}")
# print(f"The cube value is: {res[1]}")

def banner_of_the_day(message, delim = "*"):
    print(len(message) * delim)
    print(message)
    print(len(message) * delim)

# banner_of_the_day("GOOD EVENING")
# banner_of_the_day(delim= "+", message = "GOOD MORNING")






def function(*args):
    print(args)
    print(type(args))

def function_2nd(a, b, c, *args):
    print(args)
    print(a)
    print(b)
    print(c)

def function_3rd(a, b, c, **kwargs):
    print(a)
    print(b)
    print(c)
    print(kwargs)
    print(type(kwargs))
    if 'arg1' in kwargs:
        print(":)")

function_3rd("a", "b", "c", arg1 = 10, arg2 = 20)

# function_2nd(1, 2, 3, 3, 4, 5, 6)

# function()
# function(1, 2, 3, 4)
# function(1)




















