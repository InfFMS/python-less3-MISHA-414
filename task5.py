
# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, среднее арифметическое тех введённых чисел,
# которые являются степенями числа 2.
# Вывести "нет", если таких чисел нет.
from math import log


a=int(input())
summ=0
count=0
while a!=0:
    if log(a, 2)%1==0:
        summ+=a
        count+=1
    a=int(input())
if summ==0:
    print('нет')
else:
    print(f'Среднее арифметическое чисел, являющихся степенями двойки: {summ/count:.4f}')
