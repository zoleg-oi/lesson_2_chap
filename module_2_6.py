# Слишком древний шифр
import random


# Функция выдает случайным обпазом число из списка от 3 до 20
def random_first_value():
    val_nest = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    return random.choice(val_nest)


# конец random_first_value

# Функция служит для вычисления  и
# передачи списка числел на которые делится без остатка входящее значение
def remainder_division(num):
    num_rem = []
    for ii in range(3, num + 1):

        if num % ii == 0:
            num_rem.append(ii)
    return num_rem


# конец remainder_division
# Функция служит для вычисления пар в получаемых значениях
def calculating_the_pairs(num):
    pair = []
    len_rd = len(num)
    for r in range(0, len_rd):
        for i in range(1, num[r]):
            for ii in range(1, num[r]):
                pr = []
                if (i + ii == num[r]) and (i < ii):
                    pr.append(i)
                    pr.append(ii)
                    pair.append(pr)
    # сортируем полученный результат к виду, указанному в задании
    pair.sort()
    len_pair = len(pair)
    key = ''
    for lp in range(0, len_pair):
        key += str(pair[lp][0]) + str(pair[lp][1])
    return key
# Конец calculating_the_pairs

# Получаем случайное число из диапазона
rfv = random_first_value()

print('На камне в первом гнезде написано число: ' + str(rfv))
print()
# получаем все цифры для составления пароля второго гнезда
rd = remainder_division(rfv)
# вычисляем ключ по заданию, т.е. получаем список пар в отформатированном варианте
cs = calculating_the_pairs(rd)

print('А вот и ключ во второе гнездо ловушки!!!')
print()
print(cs)
