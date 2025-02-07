# match case
match a := int(input()):
    case 41:
        print('blabla')
    case 42:
        print('blinblin')
    case _:
        print(f'No case for your {a}')
