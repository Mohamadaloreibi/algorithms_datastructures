import os

search_word = input("Enter a search word: ")

list_of_files = []
for dirpath, dirnames, filenames in os.walk(
        '/Users/willi/PycharmProjects/iot22_algorithms_datastructures/Assignments/Assignment 3/'):
    list_of_files.append(filenames)

print(list_of_files)

file_list = []
for item in list_of_files:
    for j in item:
        file_list.append(j)
print(file_list)

for item in file_list:
    with open(item, encoding='utf-8') as f:
        content = f.read()
        if search_word in content:
            print(search_word, "exists in ", item)
        else:
            print(search_word, "does not exist in ", item)
#Programmet ska starta med ett meddelande som säger åt användaren att skriva in ett sökord.



#Om programmet hittar en fil som innehåller textsträngen så ska filens absoluta sökväg skrivas ut på en egen rad.




#Om filen inte innehåller textsträngen så ska ingenting skrivas ut för den filen.

#Om filen (eller en katalog) inte går att läsa så ska ett felmeddelande som minst innehåller filens/katalogens absoluta sökväg skrivas ut.