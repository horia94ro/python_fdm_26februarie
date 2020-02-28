print(7 >= 10)
print(10 != 12)
print(15 > 10)



a = 32
if (a >= 25 and a <= 30):
    print("Number in the interval")
else:
    if (a < 25):
        print("Number is smaller than 25")
    else:
        print("Number is bigger than 30")


if a >= 25 and a <= 30:
    print("Number in the interval")
elif a < 25:
    print("Number is smaller than 25")
elif a > 30:
    print("Number is bigger than 30")
else:
    print("The default case")





season = input("Enter the value: ").lower()
if season == "summer":
    print("HOT :D")
else:
    if season == "winter":
        print("COLD :(")
    else:
        if season == "fall" or season == "spring":
            print("RAIN")
        else:
            print("Invalid value for season")

if season == "summer":
    print("HOT :D")
elif season == "winter":
    print("COLD :(")
elif season == "fall" or season == "spring":
    print("RAIN :(")
else:
    print("Invalid value")


hour = input("Enter the hour: ")
if hour.isnumeric():
    hour = int(hour)
    if hour > 0 and hour <= 23:
        if hour >= 6 and hour < 12:
            print("Good morning!")
        elif hour >= 12 and hour < 17:
            print("Good afternoon!")
        elif hour >= 17 and hour <= 22:
            print("Good evening!")
        else:
            print("You should be sleeping")
    else:
        print("Value is not on the clock!")
else:
    print("The value is not correct.")


if 123:
    print(":)")

if "non empty string":
    print(":)")





a = 100
while a > 5:
    print(a, end = "\t")
    a -= 8

print("\ninstruction after the loop")



count = 15
while count: #count > 0
    count -= 1
    print(count, end = " ")
    if count == 10:
        print("Execution of loop will now stop")
        break #Break will stop the whole while loop, not just the current iteration

print("Instruction after the loop")

count = 10
while count:
    if count == 5:
        count -= 1
        continue
    print(count, end=" ")
    count -= 1











