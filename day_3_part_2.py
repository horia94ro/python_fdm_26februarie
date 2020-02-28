# my_tuple = ("python", 12.7, True, "Java")
# print(my_tuple[2])
# print(my_tuple[3:])


# my_tuple[0] = "new value" #generates a TypeError since tuples can't be modified
# my_tuple = my_tuple + (4, 5, 6)
# print(my_tuple)
# my_tuple = my_tuple + (7, ) #we're using the comma so that the interpreter knows that's a tuple
# print(my_tuple)
# print(my_tuple * 3)
# print(12.7 in my_tuple)
# print(my_tuple.count(4)) #works the same as it does on lists
# print(my_tuple.index('Java')) #same as count()
# my_set = {"PTO", 123, 17.5, True, "other value"}
# for value in my_set:
#     print(value, end = " ")
#
# # print(my_set[0]) #sets do not support indexing
# my_set.add("new value")
# my_set.add(123)
# my_set.add("bolt")
# my_set.add(10)
# print("\n", my_set)
# print(my_set.remove(123)) #remove doesn't return anything
# my_set.remove("some random value") #KeyError generated
# my_set.discard(1234) #doesn't print an error if element isn't present in the set
#
# my_set.update([7, 2, 7, 7, 3])
# print(my_set)

# set_1 = {1, 2, 3, 4}
# set_2 = {2, 3, 4, 5}
# set_3  = {6, 7, 8}
# print(set_1.intersection(set_2))
# print(set_2.intersection(set_1))
# print(set_1.difference(set_2))
# print(set_2.difference(set_1))
# print(set_3.union(set_2))



# my_dict = {'key_1' : 100,
#            'key_2' : True,
#            'key_3': 17.5}
#
# print(my_dict['key_1'])
# my_dict['key_2'] = "modified one"
# print(my_dict['key_2'])
# print(my_dict)

# product = {'price': 12.5,
#            'name' : "cola",
#            'category' : 'drinks'}
#
# product['new_key'] = 100.5
# print(product)
# product.update({'price':10.5, 'stock': False, 'new_key':10})
# print(product)

# products = [('Cola', 15), ('Fanta', 12.5), ('Sprite', 14)]
# my_products = dict(products)
# print(my_products)
#
# for value in my_products.values():
#     print(value, end = " ")
#
# print()
#
# for key in my_products.keys():
#     print(key, end = " ")
#
# print()
#
# for key, value in my_products.items():
#     print("The key is {0} and the value: {1}".format(key, value))
#
# print('Cola' in my_products)
# print(12.5 in my_products) #the IN operator is "looking" only through keys
#                            #not through the values
#
#
# del my_products['Cola']
# print(my_products)
#
# my_list = []
# while True:
#     val = input("Insert a new value to the list ")
#     if val != '':
#         my_list.append(val)
#     else:
#         break

# print(my_list)



# count = len(my_list[0])
# val = my_list[0]
# for i in my_list:
#     if len(i) > count:
#         count = len(i)
#         val = i

# for i in range(1, len(my_list)):
#     if len(my_list[i]) > count:
#         count = len(my_list[i])
#         val = my_list[i]
#
# print(f"The biggest element is {val} and its length is {count}")


# line = input("Please enter the elements separated by a whitespace ")
# my_list = line.split()
# my_dict = {}
# for elem in my_list:
#     print(elem)
# for elem in my_list:
#     if elem not in my_dict:
#         my_dict[elem] = 1
#     else:
#         my_dict[elem] += 1
##Above and below are equivalent
# for elem in my_list:
#     my_dict[elem] = my_list.count(elem)

# for key, value in my_dict.items():
#     print(f"The word {key} is repeated {value} time(s)")
# print(my_dict)


nr_seconds = 190980
# sec_min = 60
# sec_hour = 60 * sec_min
# sec_day = 24 * sec_hour
# result = ()
# values = (sec_day, sec_hour, sec_min)
# for val in values:
#     var = nr_seconds // val
#     nr_seconds = nr_seconds - var  * val
#     result = result + (var, )
# print(result)

days = int(nr_seconds / 60 / 60 / 24)
hours = int (nr_seconds / 60 / 60) - int(days * 24)
minutes = int (nr_seconds / 60) - days * 24 * 60 - hours * 60
my_tuple = (days, hours, minutes)
print(my_tuple)
















