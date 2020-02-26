# my_string = "HELLO " "WORLD"
# print(my_string)
#
# my_string_2 = "HELLO " + "WORLD"
# print(my_string_2)

# my_string_3 = "Telecom Academy"
# print(my_string_3.upper()) #the initial string is not modified
# print(my_string_3) #so the initial value will be printed
#
# my_string_4 = "METRO SYSTEMS"
# my_string_4 = my_string_4.lower()
# print(my_string_4)

# my_string_5 = "HELLO PYTHON'

# my_string_6 = "welcome to telecom academy. today is monday"
# my_string_6 = my_string_6.capitalize()
#
#
# print(my_string_6)
# print("HELLO WORLD".capitalize()) #lowercases the 2nd to the last characters
#
# my_string_7 = "   Today we're learning Python   "
#
# print(my_string_7.__len__())
# print(len(my_string_7))



my_string_8 = "today we're learning python"
# print(my_string_8.replace('java', 'c++')) #replace will not generate an error
#                             #if it can't replace anything
#
# print(my_string_8.replace('e', 'E', 2)) #3rd argument represents the number
#                             #of occurrences to replace
#

my_string_9 = "Python is a good language"
# print(my_string_9.find('o')) #index of the first appearance of the 'o' character
# print(my_string_9.find('O')) #return -1 because Python is case-sensitive
#                         #and 'O' isn't part of our string

my_string_10 = "I LIKE LEARNING PYTHON"
# my_string_10 = my_string_10.lower()
# my_string_10 = my_string_10.replace('python', 'programming')
# my_string_10 = my_string_10.upper()
# print(my_string_10.lower().replace('python', 'programming').upper())
# print(my_string_10.replace('python'.upper(), 'programming'.upper()))
# delim = "*"
#
#
# sequence = ("telecom", "metro", "python")
# print(delim.join(sequence))
#
# s1 = 'telecom'
# s2 = 'metro'
# s3 = 'python'
# print(s1 + "*" + s2 + "*" + s3)
# print(s1, s2, s3, sep = "*")

print("ANA HAS " + str(3 + 4) + " APPLES")
print("ANA HAS", (3 + 4), "APPLES")

