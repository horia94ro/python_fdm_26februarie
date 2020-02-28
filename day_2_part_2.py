# for x in range(10):
#     if x % 2 == 0:
#         print("even")
#     else:
#         print("odd")


# for count in range(10, 100, 15): #starting point | upper limit + 1 | step
#     if count == 55:
#         continue
#     print(count, end = " ")


# elements = ['telacad', 'metro', 'systems', 'cat']
# # for elem in elements:
# #     print(elem + " has the length of " + str(len(elem)))
#
# # print(elem)
# for index in range(len(elements)):
#     print(elements[index], end = "+")


##EXERCISE 1
# while True:
#     value = input("What's the name of the academy? ")
#     if value == "telacad":
#         print("End of program")
#         break

# while input("Enter the name") != "telacad":
#     continue
# print("END OF PROGRAM")
# my_string = input("Enter the value: ")
# my_string2 = "telacad"
# while my_string != my_string2:
#     my_string = input("Enter the value: ")
# print("END OF PROGRAM")


##EXERCISE 2
# my_sum = 0
# while True:
#     value = input("Write a value: ")
#     if not value.isnumeric():
#         print("Value is not numeric")
#         continue
#     value = int(value)
#     if value <=  2:
#         print("Enter a value greater than 2")
#     else:
#         break
#
# for x in range(value + 1):
#     my_sum += x
#
# print(my_sum)


##BONUS EXERCISE


# num = int(input("Enter a numerical value: "))
# if num >= 0 and num <= 100:
#     for nr in range(1, num):
#         if nr % 3 == 0 and nr % 5 == 0:
#             print(str(nr) + "FIZZ BUZZ")
#         elif nr % 3 == 0:
#             print(str(nr) + "FIZZ")
#         elif nr % 5 == 0:
#             print(str(nr) + "BUZZ")
#         else:
#             print(nr)
#

##EXERCISE 3
# x = 3
#
#
#
# if isinstance(x, int):
#     print(x + 3)
# elif isinstance(x, float):
#     print(x / 2)
# elif isinstance(x, complex):
#     print(x.real)
#     print(x.imag)
#     print(abs(x))
#



##OPTIONAL EXERCISE 1


# x = input("Enter a value: ")
# if x.isnumeric() and int(x) >= 0:
#     if int(x) % 2 == 0:
#         print("{0} is even".format(x))
#     else:
#         print("{0} is odd".format(x))
# else:
#     print("Value is either not numeric or greater than 0!")



##OPTIONAL EXERCISE 2
# prime = True
# x = int(input("Enter a value: "))
# if x > 0:
#     if x % 2 == 0 and x != 2:
#         prime = False
#     else:
#         for nr in range (3, x // 2 + 1, 2):
#             if x % nr == 0:
#                 prime = False
#                 break
#
# if prime:
#     print("Number is prime")
# else:
#     print("Number is not prime!")
#
#











