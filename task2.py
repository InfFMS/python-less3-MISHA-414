# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено двузначных натуральных чисел,
# и сколько других.
a=int(input())
two=0
no_two=0
while a!=0:
    if a>9 and a<100:
        two+=1
    else:
        no_two+=1
    a=int(input())
print(f'Двузначных чисел: {two} и Других чисел: {no_two}')

