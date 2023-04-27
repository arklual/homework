'''
Напишите программу, которая находит среднее арифметическое всех четных чисел, записанных в файле
dz3.txt чисел (числа в файле расположены в столбик), и выводит результат в файл dz2.txt в формате «Average=…».
'''
nums = []
with open('dz3.txt') as file:
    nums = list(filter(lambda x: x%2 == 0, map(int, file.readlines())))
with open('dz2.txt', 'w') as file:
    file.write(f'Average={sum(nums)/len(nums)}')