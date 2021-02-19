"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""
from cProfile import run
import timeit


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


run('revers_1(363636)')
print('revers_1', timeit.timeit('revers_1(363636)', globals=globals()))

run('revers_2(363636)')
print('revers_2', timeit.timeit('revers_2(363636)', globals=globals()))

run('revers_3(363636)')
print('revers_3', timeit.timeit('revers_3(363636)', globals=globals()))

# 1) Первая функция самая медленная, т.к. она рекурсивная
# 2) Вторая функция быстрее первой, но медленнее второй, т.к. в ней есть цикл и математические операции
# 3) Третья функция самая быстрая, в ней просто срезается строка, нету циклов и математических операций
