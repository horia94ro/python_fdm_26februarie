# my_list = [123, "some string", 15.7, True, "cat"]
# print(my_list[3])  #True
# print(my_list[2:])
#
#
# my_list[0] = "modified value"
# print(my_list)
# # print(my_list[99]) #IndexError since index 99 doesn't exist in my_list
# my_list.append("new value") #adding individual new values
# my_list.append(False)
#
# my_list = my_list + [4, 5, 6] #adding multiple new values
# print(my_list)
#
# my_list.extend([7, 8, 9]) #alternative to adding multiple new values
# print(my_list)

# second_list = ["bolt", "leia", 78.5, "cat", "bolt", 1, 1] #lists allow duplicate values to be stored
# print(second_list.remove(78.5)) #doesn't display anything is removal is successful
# # second_list.remove(123) #throws exception because element is NOT in the list
# second_list.remove("bolt") #deletes the first occurrence
# print(second_list)
#
#
# print(second_list.index("leia")) #first occurence of the element
# # print(second_list.index("modified")) #throws exception if element not present
# print("modified" in second_list)
# print("t" in "telecom academy")
# print("parrot" not in second_list)
# print(second_list.count("modified")) #number of occurences
# print(second_list.count(1))
# print(second_list)
# print(second_list.pop()) #deletes and returns the last element in the list
# print(second_list.pop(1)) #same operation for index 1
# # print(second_list.pop(99)) #IndexError
# del second_list[0] #used for removal based on index
# print(second_list)
#


# my_list = list()
# nr = int(input("How many elements do you want to add to the list? "))
# for i in range(nr):
#     val = int(input("Write the element with index {}: ".format(i)))
#     my_list.append(val)
#
# print(my_list)
# double_list = my_list.copy()
#
# for i in range(len(double_list)):
#     double_list[i] *= 2
# double_list = []
# for i in range(nr):
#     double_list.append(my_list[i] * 2)

# double_list = [i * 2 for i in my_list]
# print(double_list)

# colors = ['red', 'blue', 'green']
# result = [val.capitalize() for val in colors if len(val) == 3]
# print(result)
# nr = int(input("How many values should we add?"))
# my_list = list()
# unique_list = []
#
# for x in range(nr):
#     value = int(input("Value with index {0}: ".format(x)))
#     my_list.append(value)
#
# for elem in my_list:
#     if elem not in unique_list:
#         unique_list.append(elem)
#
# print(unique_list)


# nr = int(input("How many values should we add?"))
# my_list = list()
# real_unique = []
#
# for x in range(nr):
#     value = int(input("Value with index {0}: ".format(x)))
#     my_list.append(value)
#
# for elem in my_list:
#     if my_list.count(elem) == 1:
#         real_unique.append(elem)
#
# print(real_unique)
#

# my_list = [5, 6, 8, 1, 2, -1]
# my_list.sort()
# print(my_list)
# second_list = ['abc', 123, '789', '1', 456]
# second_list.sort()
# print(second_list)
second_list = ['5', '4', '1', '2', '3']
second_list.sort()
print(second_list)
third_list = ['leia', 'bolt', 'sheba', 'bucky', 1, 2, 3, 4]
third_list.reverse()
print(third_list)










