# import math
# def compute(x):
#     if x < 0:
#         raise ValueError("Square root can only be applied on positive values")
#     return math.sqrt(x)
#
#
# try:
#     print(compute(-1))
# except Exception as e:
#     print("An illegal operation executed: {}".format(e))
#
# print(":)")
#
# print(compute(9))


def read_elements(nr_elements):
    """
    Reads nr_elements from the user using input() method
    :param nr_elements: How many times to repeat the read operation
    :return: List with all the elements that were read from the user
    """
    initial_elements = []



    for i in range(0, nr_elements):
        initial_elements.append(input("Element {}: ".format(i)))
    return initial_elements

def convert_elements(initial_list):
    converted_list = []
    exception_list = []
    for elem in initial_list:
        try:
            elem = float(elem)
            converted_list.append(elem)
        except:
            exception_list.append(elem)

    return converted_list, exception_list


nr = int(input("Number of elements: "))
my_list = read_elements(nr)
result = convert_elements(my_list)
print("Elements that were converted: {}".format(result[0]))
print("Elements that I couldn't convert: {}".format(result[1]))
print(my_list)
print(":)")












