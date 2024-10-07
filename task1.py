#с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено положительных
# и сколько отрицательных чисел.
a=int(input())
count=0
minus=0
while a!=0:
    if a<0:
        minus+=1
    count+=1
    a=int(input())
print(count)
print(minus)
