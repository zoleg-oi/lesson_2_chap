# Условная конструкция. Операторы if, elif, else.

import sys

# Прграмма ограничевает сравнение только типом integer
def input_user(input_int):# Определяем правильность ввода
    try:
        int_input_int = int(input_int)
        return 1
    except:
        return 0
# end input_user



max_in = 3 # Максимальное значение неверных вводов

n = 0
while n <= max_in:
    first = input('Введите первое целое число: ')
    res = input_user(first)
    if res == 1:
        break
    else:
        n += 1
        print('Введите целое число, осталось попыток - ' + str(max_in - n))
        if n == max_in:
            print('Вы ввели максимальное значение неверных значений')
            sys.exit()

n = 0
while n <= max_in:
    second = input('Введите первое целое число: ')
    res = input_user(second)
    if res == 1:
        break
    else:
        n += 1
        print('Введите целое число, осталось попыток - ' + str(max_in - n))
        if n == max_in:
            print('Вы ввели максимальное значение неверных значений')
            sys.exit()

n = 0
while n <= max_in:
    third = input('Введите первое целое число: ')
    res = input_user(third)
    if res == 1:
        break
    else:
        n += 1
        print('Введите целое число, осталось попыток - ' + str(max_in - n))
        if n == max_in:
            print('Вы ввели максимальное значение неверных значений')
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
# Но можно сделать в два этапа и будет работать, но, с моей точки зрения, очень громоздко
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
