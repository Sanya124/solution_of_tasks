from src.dzen_task import *


def main():
    number = int(input('Введите номер задания (от 1 до 7): '))

    if number == 1:
        res = min_nat_num(int(input('1. Введите число: ')))
        print(f'1. Ответ: {res} - минимальное натуральное число') if type(res) == int else print(res)

    elif number == 2:
        print('2. Ответ:', not_leap())

    elif number == 3:
        print('3. Ответ:', diving_17_and_19(int(input('3. Введите число: '))))

    elif number == 4:
        print('4. Ответ:', does_not_end_on_3_and_9(int(input('4. Введите число: '))))

    elif number == 5:
        print('5. Ответ:', sum_except_3_or_7(int(input('5. Введите число: '))))

    elif number == 6:
        print('6. Ответ:', multi_except_num_div_2_or_3(int(input('6. Введите число: '))))

    elif number == 7:
        res = not_contains_3(int(input('7. Введите число: ')))
        print('7. Ответ:', res) if type(res) == int else print(res)

    else:
        print('Введён неправильный номер задачи')


if __name__ == '__main__':
    main()
