# my_binary = 0b1001001
# print(my_binary)
#
#
#
# my_octal = 0o100612
# print(my_octal)
#
# my_hexa = 0xFA01
# print(my_hexa)
# FINAL_VALUE = 10 #we don't have final keyword in Python
#             #final values are marked with uppercase letters
#
# my_float = 3e3 #e is followed by the exponential value
# print(my_float)

# my_complex = 7 + 5j
# print(my_complex.real)
# print(my_complex.imag)
# print(abs(my_complex))
# print(pow(7, 3)) # 7 ** 3
# print(my_complex.conjugate())

# my_name = input("Please, input your name: ")
# print("Nice to meet you,", my_name)


# print("Please enter the values")
# first_value = int(input("X: "))
# second_value = int(input("Y: "))
# print("The sum of the values is:", first_value + second_value)
# import getpass
#
# username = input("Please enter your username: ")
# input()
# password = getpass.getpass("Please enter password: ")
# print(username, password)
#


##EXERCISE 1
# my_string = input("Please insert the name of the academy: ")
# my_string = my_string + " Academy teaches Python "
# my_string = my_string + str(3)
# my_string = my_string + " because Python 2 is no longer supported in 2020"
# print(my_string)
# print("Telecom Academy teaches Python %i because Python %i is obsolete" % (3, 2))

##EXERCISE 2
# my_float = float(input("Write float number"))
# my_complex_real = float(input("Write real part of the complex number"))
# my_complex_imag = float(input("Write imaginary part of the complex number"))
# my_complex = complex(my_complex_real, my_complex_imag)
# my_sum = my_float + my_complex
# print("Real part of sum: %f and this is awesome" % my_sum.real)
# print("Imag part of sum: %f" % my_sum.imag)
# print("Module: %f" % abs(my_sum))

##EXERCISE 5
# message = "Telecom Academy is teaching a lot of online courses"
# message = message.replace("teaching", "oferring")
# print(message)

##EXERCISE 7
# colors = "blue,red,green"
# result = colors.split(",")
# print(result)
##The operation above and below are opposite to one another
delim = ","
colors = ("blue", "red", "green")
print(delim.join(colors))