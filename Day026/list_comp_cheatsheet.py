
# # Wenn wir durch eine Liste iterieren und auf alle Inhalte 1 addieren möchten sieht die normale schleife so aus
# numbers = [1, 2, 3]
# new_list = []
#
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# print(new_list)
#
#
# # In Python gibt es dafür die List Comprehension.
# # Merksatz dafür ist [new_item for item in list]
# new_list = [n + 1 for n in numbers]
# print(new_list)
#
# # Das gilt nicht nur für Listen, sondern funktioniert auch mit Strings.
# # Wir können jeden einzelnen Buchstaben als ein Element in die Liste nehmen
# name = "Christian"
# name_list = [letter for letter in name]
# print(name_list)
#
# # Wir können auch mit anderen Sequences arbeiten. (range, tuple)
# count_list =  [n * 2 for n in range(1, 5)]
# print(count_list)
#
# # Das ganze funktioniert auch mit Conditions. Wir können auch mit "if" arbeiten.
# # Wir nehmen alle Namen aus der Liste und geben nur die wieder die weniger als 5 Zeichen haben.
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
#
# # Wir können auch alle Namen in Uppercase ausgeben mit der Comprehension.
# # So wie oben nur, dass alle names durch die upper() methode laufen.
# capital_short_names = [name.upper() for name in names if len(name) < 5]
# print(capital_short_names)
#
#
# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(n) for n in list_of_strings]
# print(numbers)
# result = [n for n in numbers if n % 2 == 0]
# print(result)


# # Ein Beispiel wie man die beiden listen in den txt files auslesen kann und checken kann, welche Nummern diese gemeinsam haben
# list1 = open("file1.txt").readlines()
# list2 = open("file2.txt").readlines()
#
# result = [int(n) for n in list1 if n in list2]
# print(result)