def test(value, *types, **values):
    print('Тип:', type(values))
    print('ФИО:', values)
    print('Полных лет:', value)
    print(types)


test(25, 11, 'April', 1999, surname='Харламов', name='Дмитрий', patronymic='Борисович')


def summa(n=6):
    if n == 0:
        return 0
    else:
        return n + summa(n - 1)


print(summa())
