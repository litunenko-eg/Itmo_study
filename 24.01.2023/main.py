#1 task
print('Задание 1. Строка \'Python is the best programming language in the world\' с 6го символа по -7й:')
str = 'Python is the best programming language in the world'
str1 = str[5:-7]
print(str1)
print()

print('Задание 2. Каждый третий символ строки \'Guido van Rossum is the benevolent dictator for life\':')
str = 'Guido van Rossum is the benevolent dictator for life'
str1 = str[::3]
print(str1)
print()

print('Задание 3. Из строки \'You have a problem with authority, Mr. Anderson.\' получить словарь, где ключ -это символ, \nа значение - это количество повторений символа в строке:')
str = 'You have a problem with authority, Mr. Anderson.'
s = set(str)
listt = list(str)
m = list(map(listt.count, s))
d = dict(zip(s, m))

d1 = dict(zip(set(str), list(map(listt.count, s))))

print(d)
print (d1)
print(d == d1)