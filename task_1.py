#Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

#filter применяет функцию ко всем элементам последовательности 
# и возвращает итератор с теми объектами, для которых функция вернула True.

#list comprehension генератор списков.

#map применяет какую-либо функцию к каждому элементу списка своих аргументов,
# выдавая список результатов как возвращаемое значение.

#enumerate (sequence, start = 0) применяется в случаях, когда необходим счётчик количества элементов в 
# последовательности.Позволяет избавиться от необходимости инициировать и обновлять
#  отдельную переменную-счётчик.Выдает объект итератор, который мы можем перебирать

# n = int(input('N:'))
# list = [i for i in range(-n,n+1)] # list comprehension 
# print (f'генерация списка: {list}')

A = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
print (f'список A :{A}')

# print(f'элементы списка А по модулю:{(list(map(abs,A)))}') #map

# B = [i for i in A if i%2 == 0] # list comprehension 
# print (f'четные элементы А: {B}')# list comprehension 

# print (type(A[0]))
# print (f'четные элементы А: {list(map(lambda i: (i%2 ==0), A))}') #map #lambda
# print (f'четные элементы А: {list(filter(lambda i: (i%2 ==0), A))}') #filter #lambda

# print(f'возведение в квадрат элементов списка A:{(list(map(lambda A: A**3,A)))}')#map #lambda


# # print (A[7::]) # срез списка

# # def sum_A(A) -> int: #метод сумма элементов списка
# #     sum = 0
# #     for i in A:
# #         sum += i
# #     return sum
# # print (f'сумма элеметов списка: {sum_A(A)}')



# def has_o(string):
#     return 'o' in string.lower()
# List = ['One', 'two', 'three', '23gfyug']
# print(f'слово содержит буку o: {list(filter(has_o,List))}') #filter
# print(list(filter(lambda string:'o' in string.lower(),List)))  #filter  #lambda
# print(f'слово содержит буку o:{[string for string in List if has_o(string)]}') # list comprehension

# #zip Функция zip() создает итератор кортежей, который объединяет элементы каждой
# # из переданных последовательностей *iterables . Функция zip() возвращает итератор кортежей, 
# # где i-й кортеж содержит i-й элемент из каждой итерации аргументов. Сам определяет длину 
# # наименьшей последовательности

# a = [5,6,7]
# b = [100, 200, 300, 40]
# c = 'ahsh'
# print(f'функция zip: {list(zip(a,b))}') #zip

# # rez = zip(a,b,c) # кортежи
# # col1,col2,col3 = zip(*rez) #* делает распаковка *rez
# # print(col1,col2,col3)

# print (f'функция enumerate:{list(enumerate(a))}')# создает кортежи их индекса и элемента списка
# for index, value in enumerate (a):
#     print(f'функция enumerate:{index,value}')

# for index, value in enumerate (range(10,20)):#создает список от 10 до 20
#     print(f'функция enumerate:{index,value}')

# for index, value in enumerate (a,20):#создает список a, номерация начинается с 20
#     print(f'функция enumerate:{index,value}')

# for e in enumerate (a):#обходит список объектов по индексу
#     print(f'функция enumerate:{e}')


