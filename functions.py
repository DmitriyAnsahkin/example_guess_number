import random


def read_input_number() -> int:
    """Метод предлагает пользователю ввести в консоль целое число, обрабатывает ввод и возвращает это число.

    Returns:
        input_number: введенное число.
    """

    input_correctly = False
    input_number = None

    while input_correctly is False:
        try:
            input_number = int(input("Введите число: "))
            input_correctly = True

        except ValueError:
            print('Введите, пожалуйста число!')
            input_correctly = False

    return input_number


def compare_numbers(input_number: int, hidden_number: int) -> bool:
    """Метод сравнивает два целых числа и возвращает результат сравнения

    Args:
        input_number: введенное пользователем число.
        hidden_number: число сгенерированное системой, которое должен угадать пользователь.

    Returns:
        win: результат сравнения двух переменных
    """
    if input_number == hidden_number:
        print('Победа!')
        win = True

    else:
        print('Введенное число больше загаданного') if input_number > hidden_number \
            else print('Введенное число меньше загаданного')
        win = False

    return win


def game(counter=3, hidden_number=None):
    """Метод считывает с консоли вводимое число и сравнивает его с hidden_number.

    Args:
        counter: количество попыток угадать число.
        hidden_number: загаданное число, с которым будет сравниваться ответ пользователя.

    """

    win = False

    if hidden_number is None:
        hidden_number = random.randrange(0, 10)

    print('Система сгенерировала случайное число. Количество попыток: {n}'.format(n=str(counter)))

    while win is False and counter != 0:
        input_number = read_input_number()

        win = compare_numbers(input_number=input_number, hidden_number=hidden_number)

        if win is False:
            counter -= 1
            print(f'Осталось попыток: {counter}')
    print('Загаданное число: ' + str(hidden_number))


def read_input_continue_game() -> str:
    """Метод выводит в консоль предложение продолжить игру и возвращает введенный ответ

    Returns:
        input_response: введенное пользователем значение.
    """
    input_correctly = False

    while input_correctly is False:
        input_response = str(input('Продолжить? (y/n): '))

        if input_response != 'y' and input_response != 'n':
            print('Ошибка. Попробуйте ввести один из предложенных вариантов.')

        else:
            input_correctly = True

            return input_response
