# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено простых натуральных чисел
# (которые делятся только сами на себя и на 1), и сколько составных.
a=int(input())
lst=[]
ma=0
while a!=0:
    if a>ma:
        ma=a
    lst.append(a)
    a=int(input())

def resheto(N):    # Решето эратосфена
    primes = [i for i in range(N + 1)]
    primes[1] = 0
    i = 2
    while i <= N:
        if primes[i] != 0:
            j = i + i
            while j <= N:
                primes[j] = 0
                j = j + i
        i += 1

    return [i for i in primes if i != 0]
if ma==0:
    print(f'Простых чисел: {0} и Составных чисел: {0}')
else:
    p=resheto(ma)
    count=0
    no_count=0
    for num in lst:
        if num in p:
            count+=1
        else:
            no_count+=1
    print(f'Простых чисел: {count} и Составных чисел: {no_count}')






