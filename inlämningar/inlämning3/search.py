


import os

search_word = input("Enter a search word: ")

file_list = []
for dirpath, dirnames, files in os.walk(
        '/Users/willi/PycharmProjects/iot22_algorithms_datastructures/Assignments/Assignment 3/'):
    for file in files:
        file_list.append(os.path.join(dirpath, file))

print(file_list)


def search_for_word(num = 0):
    """Loop through a file and search for the word"""

    with open(file_list(0), encoding='utf-8') as f:
        content = f.read()
        if search_word in content:
            return print(search_word, "exists in ", file)
        else:
            print(search_word, "does not exist in ", file)
            return search_word()



if __name__ == '__main__':
    search_for_word()
"""
file = open("search.txt")
    print(file.read())
    search_word = input("enter a word you want to search in file: ")
    if(search_word ==  file):
        print("word found")
    else:
        print("world not found")
        """

