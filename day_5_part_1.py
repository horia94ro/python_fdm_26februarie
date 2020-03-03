def modify(x):
    print("Location inside the method: ",id(x))
    print("Value inside the method: ", x)
    x += 1
    print("Location inside the method: ", id(x))
    print("Value inside the method: ", x)

def modify_list(my_list):
    print("Location inside the method: ", id(my_list))
    print("Value inside the method: ", my_list)
    my_list.append("new value")
    print("Location inside the method: ", id(my_list))
    print("Value inside the method: ", my_list)

# value = 10
# print("Location in main program: ", id(value))
# print("Value in the main program: ", value)
# modify(value)
# print("Location in main program: ", id(value))
# print("Value in the main program: ", value)
# values = [2, 4, 6]
# print("Location in main program: ", id(values))
# print("Value in the main program: ", values)
# modify_list(values)
# print("Location in main program: ", id(values))
# print("Value in the main program: ", values)




count = 10


def get_count():
    count = 5
    print(count)
    # return (count)

def set_count(c):
    global count
    count = c
    print(count)

# get_count()
# print(count)
# print(count)
# set_count(100)
# print(count)

def function_one():
    print(":)")
    def nested_function():
        x = 10
        print("I'm inside a nested function")
    # print(x)
    return nested_function


# res = function_one()
# print(type(res))
# res()

print(open)
open = "modified value valuevaluevaluevaluevaluevaluevaluevaluevaluevaluevaluevaluevaluevaluevalue "
print(open)





















