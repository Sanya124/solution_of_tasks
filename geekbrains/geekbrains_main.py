from geekbrains.src.geekbrains_task import *
from geekbrains.src.private_raise import private_raise


def main():
    number = int(input('Введите номер задания (от 1 до 10): '))

    if number == 1:
        res = day_off(int(input('Введите номер дня недели: ')))
        if 0 < res < 8:
            print('День выходной') if res else print('День рабочий')
        else:
            print(private_raise(el='номер недели', val='[1:7]'))

    elif number == 2:
        [print(x) for x in truth_of_statement()]

    elif number == 3:
        x = int(input('Введите первую координату: '))
        y = int(input('Введите вторую координату: '))
        if x == 0 or y == 0:
            print('Координата или координаты нулевые')
        else:
            print(f'Номер четверти {number_quarter_of_plane(x=x, y=y)}')

    elif number == 4:
        quarter = int(input('Введите номер четверти: '))
        if 0 < quarter < 5:
            print(f'Номеру четверти {quarter} соответствует диапазон "{range_coordinates_of_points(quarter)}"')
        else:
            print(private_raise(el='номер четверти', val='[1:4]'))

    elif number == 5:
        x1 = int(input('Введите первую координату первой точки: '))
        y1 = int(input('Введите вторую координату первой точки: '))
        x2 = int(input('Введите первую координату второй точки: '))
        y2 = int(input('Введите вторую координату второй точки: '))
        diff = distance_between_points(x1=x1, y1=y1, x2=x2, y2=y2)
        print(f'Расстояние между точками {diff:.3f}')

    elif number == 6:
        res = sum_of_digits_of_number(input('Введите вещественное число: '))
        print(f'Сумма цифр введённого числа равна {res}')

    elif number == 7:
        n = int(input('Введите число для поиска набора проиведений числа: '))
        if n >= 0:
            set_number = ', '.join([str(x) for x in list_factorial(n)])
            print(f'Набор произведений числа {n}: {set_number}')
        else:
            print(private_raise(el='число', val='[1:∞)'))

    elif number == 8:
        n = int(input('Введите число для последовательности: '))
        if n > 0:
            print('Сумма списка равна', sum_of_list_to_formula(n))
        else:
            print(private_raise(el='число', val='[1:∞)'))

    elif number == 9:
        count = int(input('Введите количество чисел и диапазон (одним числом), не менее 6: '))
        # В data/file.txt есть числа 1, 3 и 5. Если ввести число менее 6, то будет "IndexError: list index out of range"
        if count > 5:
            print('Произведение элементов из файла:', multi_of_list_items(count))
        else:
            print(private_raise(el='число и диапазон', val='[6:∞)'))

    elif number == 10:
        list_of_numbers = input('Введите список чисел, разделённых пробелом: ').split(' ')
        print('Перемешанный список:', ' '.join(shuffle_list(list_of_numbers)))

    else:
        print(private_raise(el='номер задания', val='[1:10]'))


if __name__ == '__main__':
    main()
