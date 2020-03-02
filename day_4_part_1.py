# products = {
#     'food':10,
#     'electronics':19,
#     'houses' : 7
#     # 'other'
# }
# def calculate_vta(product_type = 'other', inital_value = 1):
#     final_value = inital_value + inital_value / 20
#     if product_type in products:
#         final_value = final_value + final_value * products[product_type] / 100
#     else:
#         final_value = final_value + final_value * 0.1
#     return final_value, 100
#
# intial_value = int(input("Enter the initial value: "))
# product_type = input("Enter product type: ")
# # print(calculate_vta(inital_value = 100, product_type = 'food' ))
# # print(product_type)
# final_value = calculate_vta(product_type, intial_value)
# print("The initial value was: {}".format(intial_value))
# print("The final value was: {}".format(final_value))
# print("The category of the product was: {} ".format(product_type))

x = 10
y = 3
try:
    res = x / y
    print(res)


    my_list = [1, 2, 3]
    # print(my_list[99])
    print(":)")
    a = int("abc")
    print(":(")


except ZeroDivisionError:
    print("You divided by 0, you moron!")
except IndexError:
    print("You've used an inexistent index!")
except Exception as e:
    print("The general case of exceptions!", str(e))
else:
    print("Instructions executed only when NO exception is thrown!")
finally:
    print("Instructions executed no matter what!")

























