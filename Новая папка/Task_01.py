# https://drive.google.com/file/d/1IPu_RRcw_RI6Duecn-9q2Z3xMmfKM5fe/view?usp=sharing


# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа должна не завершаться, а запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа сообщает ему об ошибке и снова запрашивает знак операции.
# Также пользователю нужно сообщать о невозможности деления на ноль, если он ввел 0 в качестве делителя.



while True:
    try:
        number1, operation, number2 = [
                i for i in
                input(
                    'Введите математическое выражение (число операнд число): '
                    ).split()
                ]
    except ValueError:
        print('Неправильный ввод.')
        continue
    number1 = int(number1)
    number2 = int(number2)

    if operation == '0':
        break
    elif operation == '+':
        print(f'{number1} {operation} {number2} = {number1 + number2}')
    elif operation == '-':
        print(f'{number1} {operation} {number2} = {number1 - number2}')
    elif operation == '*':
        print(f'{number1} {operation} {number2} = {number1 * number2}')
    elif operation == '/':
        try:
            print(f'{number1} {operation} {number2} = {number1 / number2}')
        except ZeroDivisionError:
            print('Ошибка. Деление на ноль')