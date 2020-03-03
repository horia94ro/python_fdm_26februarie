import sys

def read_words(file_name):
    all_words = []
    try:
        with open(file = file_name, mode = "rt") as file:
            for line in file.readlines():
                for word in line.split():
                    all_words.append(word)

        return all_words
    except FileNotFoundError:
        with open(file = file_name, mode = "wt") as file:
            file.write("This file was created automatically")
        return read_words(file_name)

def print_words(all_words):
    for word in all_words:
        print(word)



"""
__name__ has the value of:
1. __main__ when the words.py file is directly executed from PyCharm/cmd
2. words when the words.py module is imported to another file
"""
if __name__ == "__main__":
    # print(sys.argv)
    my_word = read_words(sys.argv[1])
    print_words(my_word)