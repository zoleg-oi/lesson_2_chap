# Условная конструкция. Операторы if, elif, else.
import sys

# Проверим правильность ввода
n = 0
while n <= 10:
    try:
        first = input('Введите первое число: ')
        int_first = int(first)
        break
    except:
        print('Это не число, введите число')
        n += 1
        if n == 3:
            print('Вы использовали все свои попытки ввода первого ЧИСЛА')
            sys.exit()

while n <= 10:
    try:
        second = input('Введите второе число: ')
        int_first = int(second)
        break
    except:
        print('Это не число, введите число')
        n += 1
        if n == 3:
            print('Вы использовали все свои попытки ввода вторго ЧИСЛА')
            sys.exit()
n = 0
while n <= 10:
    try:
        third = input('Введите третье число: ')
        int_first = int(third)
        break
    except:
        print('Это не число, введите число')
        n += 1
        if n == 3:
            print('Вы использовали все свои попытки ввода третьего ЧИСЛА')
            sys.exit()
# Строки тоже можно сравнивать, выше ограничен ввод всего кроме integer
print('Первый вариант выполнения задачи')
print()

if first == second == third:
    print(3)
elif first == second:
    print(2)
elif first == third:
    print(2)
elif second == third:
    print(2)
else:
    print(0)

# Конструкция first == second == third вполне рабочая
# Но можно сделать в два этапа и будт работать, но, с моей точи зрения, очень громоздско
print()
print('Второй вариант выполнения задачи')
print()
flag = 0

if first == second:
    if second == third:
        if first == third:
            flag = 1
            print(3)
if flag == 0:
    if first == second:
        print(2)
    elif first == third:
        print(2)
    elif second == third:
        print(2)
    else:
        print(0)

# Можно решить задачу третьим способом используя свойства множеств
# Мне так больше нравится
print()
print('Третий вариант выполнения задачи')
print()
set_input = set()
set_input.update(first, second, third)
if len(set_input) == 1:
    print(3)
elif len(set_input) == 2:
    print(2)
else:
    print(0)
