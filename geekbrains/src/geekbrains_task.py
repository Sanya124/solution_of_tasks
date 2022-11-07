import random  # Для заданий 9 и 10


# Задание 1
def day_off(day_of_week: int) -> bool:
    """ Функция для определения является ли день выходным

    Args:
        day_of_week: int, от 1 до 7
    """
    return True if day_of_week == 6 or day_of_week == 7 else False


# Задание 2
def truth_of_statement() -> list:
    """ Функция для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z на всех значениях предиката """
    total = []
    predicate = [False, True]
    for X in predicate:
        for Y in predicate:
            for Z in predicate:
                left = not (X or Y or Z)
                right = not X and not Y and not Z
                total.append(f'{left == right} --> ¬({X} ⋁ {Y} ⋁ {Z}) = ¬{X} ⋀ ¬{Y} ⋀ ¬{Z}')

    return total


# Задание 3
def number_quarter_of_plane(x: int, y: int) -> int:
    """ Функция для определения номера четверти, в которой находится точка с переданными координатами

    Args:
        x: координата на оси X
        y: координата на оси Y
    """
    if x > 0:
        return 1 if y > 0 else 4
    elif x < 0:
        return 2 if y > 0 else 3


# Задание 4
def range_coordinates_of_points(quarter: int) -> str:
    """ Функция для определения диапазона возможных координат точек в переданной четверти

    Args:
        quarter: четверть плоскости
    """
    quarter_ranges = {
        1: 'x=[0;∞), y=[0;∞)',
        2: 'x=(-∞;0], y=[0;∞)',
        3: 'x=(-∞;0], y=(-∞;0]',
        4: 'x=[0;∞), y=(-∞;0]'
    }

    return quarter_ranges[quarter]


# Задание 5
def distance_between_points(x1: int, y1: int, x2: int, y2: int) -> float:
    """ Функция для вычисления расстояния между точками в 2D пространстве

    Args:
        x1: координата на оси X первой точки
        y1: координата на оси Y первой точки
        x2: координата на оси X второй точки
        y2: координата на оси Y второй точки
    """
    res = ((x1 - x2) ** 2) + ((y1 - y2) ** 2)

    return res ** 0.5


# Задание 6
def sum_of_digits_of_number(number: str) -> int:
    """ Функция вычисления суммы чисел вещественного числа

    Args:
        number: число с раздлелителем точка или запятая
    """
    res = [int(i) for i in number if i != '.']

    return sum(res)


# Задание 7
def list_factorial(number: int) -> list:
    """ Функция выдает набор произведений чисел от 1 до N

    Args:
        number: граничное значение для набора от 1 до этой самой границы
    """
    # Переделать функцию на рекурсию
    result = []
    for i in range(1, number+1):
        if i > 1:
            result.append(result[-1] * i)
        else:
            result.append(1)

    return result


# Задание 8
def sum_of_list_to_formula(number: int) -> float:
    """ Функция суммы из n чисел последовательности (1+1/n)^n

    Args:
        number: количество последовательностей
    """
    result = [_limit(i) for i in range(1, number + 1)]
    return round(sum(result), 3)


# Задание 9
def multi_of_list_items(N: int, file='data/file.txt'):
    """ Функция нахождения произведения элементов на указанных позициях из файла

    Args:
        N:      количество чисел для генерации
        file:   путь к файлу
    """
    result = 1
    list_ = [random.randrange(-N, N + 1) for _ in range(N)]
    with open(file, 'r') as f:
        for i in f: # Значения в файле 1, 3 и 5
            result *= list_[int(i)]

    return result


# Задание 10
def shuffle_list(list_: list):
    """ Функция перемешивания списка

    Args:
        list_: список значений для перемешивания
    """
    return random.sample(list_, len(list_))


def _limit(n: int):
    """ Функция вычисляет случай последовательности по формуле (1+1/n)^n

    Args:
        n: число для вычисления случая последовательности
    """
    return (1 + (1 / n)) ** n
