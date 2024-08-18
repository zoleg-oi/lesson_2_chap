# Условная конструкция. Операторы if, elif, else.

first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

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
set_input.update(str(first),str(second),str(third))
if len(set_input) == 1:
    print(3)
elif len(set_input) == 2:
    print(2)
else:
    print(0)
