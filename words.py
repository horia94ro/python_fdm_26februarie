def read_words(file_name):
    all_words = []
    with open(file = file_name, mode = "rt") as file:
        for line in file.readlines():
            for word in line.split():

                all_words.append(word)

    return all_words

def print_words(all_words):
    for word in all_words:
        print(word)


# print(__name__)
"""
__name__ has the value of:
1. __main__ when the words.py file is directly executed from PyCharm/cmd
2. words when the words.py module is imported to another file
"""
if __name__ == "__main__":
    my_word = read_words("test.txt")
    print_words(my_word)