first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (len(x) - len(y) for x, y in zip(first, second)if len(x) != len(y))


#Функция zip в Python используется для объединения двух или более списков в один. Она возвращает итератор кортежей, где i-ый кортеж содержит i-ый элемент из каждого из переданных списков.

second_result = (len(first[i]) == len (second[i])for i in range (len(first)))

print(list(first_result))
print(list(second_result))