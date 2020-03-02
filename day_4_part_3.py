# file = open(file = "test.txt", mode = "wt", encoding = "utf-8")
# file.write("Content for the first line")
# file.write("\nWill this be on the next line?\n")
# file.write("This wil surely be on the third line!\n")
# file.writelines(['text from a new line\n', 'second new line\n', 'third'])
# print(file.closed) #checks if the file is closed or not
# file.close()
# print(file.closed)
# file.write("new line") #ValueError since the file closed

# file = open(file = "test.txt", mode = 'rt', encoding = "utf-8")
# print(file.read(10))
# print(file.read(3))
# print(file.read())
# file.seek(0)
# print(file.readline())
# print(file.readlines())
# file.close()

# file = open(file = "test.txt", mode = "a+")
# file.write("\na new hope")
# file.seek(0)
# print(file.read(100))
# file.close()

# with open('test.txt') as file:
#     print(file.readline())

# file.read() #ValueError since I can not perform an operation on a closed file


def open_file(file_name):
    with open(file = file_name, mode = "w") as file:
        file.write('first line\n')
        file.write('second line\n')
        file.write('third line\n')



open_file('exercise.txt')
file = open(file = 'exercise.txt', mode = "at")
file.writelines(['new line without context manager\n', 'last line'])
file.close()

file = open(file = 'exercise.txt')
lines = file.readlines()
for line in lines:
    print(line, end = "")





