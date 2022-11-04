from typing import Union


# Задача 7
def not_contains_3(n) -> Union[int, str]:
    """ Функция определения количества чисел от 1 до n, в записи которых нет цифры 3

    Args:
        n: натуральное число
    """
    result = 0
    if 9 < n < 100:
        for i in range(10, n + 1):
            if (i % 10) != 3 and (i // 10) != 3:
                result += 1

        return result
    else:
        return 'Необходимо ввести двузначное число'


# Задача 6
def multi_except_num_div_2_or_3(n) -> int:
    """  Функция произведения всех чисел от 1 до n, кроме тех, что делятся на 2 или на 3.

    Args:
        n: натуральное число
    """
    result = 1
    if n > 1:
        for i in range(1, n + 1):
            if not (_diving(i, 2) or _diving(i, 3)):
                result *= i
    else:
        result = 0
    return result


# Задача 5
def sum_except_3_or_7(n) -> int:
    """ Функция суммирования всех чисел от 1 до n, кроме тех, что делятся на 3 или на 7.

    Args:
        n: натуральное число
    """
    result = 0
    for i in range(1, n + 1):
        if not (_diving(i, 3) or _diving(i, 7)):
            result += i

    return result


# Задача 4
def does_not_end_on_3_and_9(n) -> int:
    """ Функция определения кол-ва удовлетворяющих условию чисел от 1 до n:
            - i-1 не заканчивается на 3,
            - i+1 не заканчивается на 9.

    Args:
        n: натуральное число
    """
    result = 0
    for i in range(1, n + 1):
        if ((i - 1) % 10 != 3) and ((i + 1) % 10 != 9):
            result += 1

    return result


# Задача 3
def diving_17_and_19(n) -> int:
    """ Функция определения кол-ва чисел от 1 до n включительно, которые удовлетворяют требованиям:
            - число оканчивается на 1
            - число делится на 17
            - число делится на 19

    Args:
        n: натуральное число
    """
    result = 0
    for i in range(1, n + 1):
        if i % 10 == 1 and _diving(i, 17) and _diving(i, 19):
            result += 1

    return result


# Задача 2
def not_leap() -> int:
    """ Функция считает количество невисокосных лет в первых 20 веках нашей эры """
    result = 0
    i: int = 1
    while i <= 2000:
        if i % 400 == 0 or (i % 4 == 0 and i % 100 != 0):
            result += 1
        i += 1

    return 2000 - result


# Задача 1
def min_nat_num(n) -> Union[int, str]:
    """ Функция определяет минимальное натуральное число такое, что:
            если от этого числа отнять 7, то оно разделится на 7;
            если отнять 8, то оно разделится на 8;
            если отнять n, то оно разделится на n.

    Args:
        n: натуральное число
    """
    i = 1
    try:
        while True:
            if _minus_and_diving(i, 7):
                if _minus_and_diving(i, 8):
                    if _minus_and_diving(i, n):
                        return i
            i += 1
    except ZeroDivisionError:
        return 'Необходимо вводить целочисленное число от 1 до бесконечности'


def _diving(num1: int, num2: int) -> bool:
    """ Вспомогательная функция для определения делится ли число num1 нацело на num2 """
    return (num1 % num2) == 0


def _minus_and_diving(num: int, operand: int) -> bool:
    """ Вспомогательная функция для определения делится ли число за вычетом operand от num на operand нацело """
    return _diving((num - operand), operand)
