# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить минимальное и максимальное из введённых чисел.
a=int(input())
if a==0:
    print('Нет чисел для анализа.')
else:
    ma=a
    mi=a
    while a!=0:
        if a>ma:
            ma=a
        elif a<mi:
            mi=a
        a=int(input())

    print(f'Минимальное число: {mi}')
    print(f'Максимальное число: {ma}')
