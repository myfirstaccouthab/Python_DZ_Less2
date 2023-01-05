# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

# n = 12345
# b= str(n)
# suma = sum (int(i) for i in b)
# print (suma)

def flo_Sum ():

    num = float(input('Enter your number, please: '))
    while  num % 10 > 0:
        num = num * 10
    return num
flo_Sum()

n = round(flo_Sum())
b= str(n)
suma = sum (int (i) for i in b)

print (suma)

# print(type(flo_Sum))


        


# for i in list:
#     new_Sum = sum (list)
# print (new_Sum)