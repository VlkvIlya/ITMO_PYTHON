RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
BLACK = '\u001b[48m'
END = '\u001b[0m'



# №1 Флаг----------------------------------------------------------------------------

def flag():
    line = ' ' * 4
    lenght = 12
    height = lenght
    for i in range(lenght):
        print(f'{BLUE}{line * (lenght // 3)}{WHITE}{line * (lenght // 3)}{RED}{line * (lenght // 3)}{END}')

#flag()

# №2 Узор----------------------------------------------------------------------------

def sign():
    line = ' ' * 3
    size = 1 # сторона пикселя
    lenght = 3 # сторона узора
    height = lenght
    for i in range(lenght):
        if i % 2 != 0:
            for i in range(size):
                if lenght % 2 == 0:
                    print(f'{WHITE}{line * size}{BLACK}{line * size}{END}' * (lenght // 2))
                else:
                    print(f'{WHITE}{line * size}{BLACK}{line * size}{END}' * (lenght // 2) + f'{WHITE}{line * size}{END}')
        else:
            for i in range(size):
                if lenght % 2 == 0:
                    print(f'{BLACK}{line * size}{WHITE}{line * size}{END}' * (lenght // 2))
                else:
                    print(f'{BLACK}{line * size}{WHITE}{line * size}{END}' * (lenght // 2) + f'{BLACK}{line * size}{END}')

#sign()

# №3 Функция----------------------------------------------------------------------------

def func():
    line = ' ' * 3
    mind_line = ' '
    for y in range(64, 0, -1):
        if y <= 9:
            x = y ** 0.5
            if x == int(x):
                print(f'\t{y}) {WHITE}{line * (int(x) - 1)}{BLACK}{line}{WHITE}{line * (10 - int(x))}{END}')
            else:
                print(f'\t{y}) {WHITE}{line * (int(x) - 1) + mind_line * 2}{BLACK}{mind_line}{WHITE}{line * (10 - int(x))}{END}')
        else:
            x = y ** 0.5
            if x == int(x):
                print(f'\t{y}){WHITE}{line * (int(x) - 1)}{BLACK}{line}{WHITE}{line * (10 - int(x))}{END}')
            else:
                print(f'\t{y}){WHITE}{line * (int(x) - 1) + mind_line * 2}{BLACK}{mind_line}{WHITE}{line * (10 - int(x))}{END}')
    print('\t0\t1  2  3  4  5  6   7   8   9')

#func()

# №4 Условие----------------------------------------------------------------------------

file = open("sequence.txt")

def zxc():
    cnt_minus = 0
    cnt_plus = 0
    for i in file:
        if float(i) > 0:
            cnt_plus += 1
        else:
            cnt_minus += 1
    print("(+)", cnt_plus, "(-)",  cnt_minus)
    print(f"+){RED}{" " * cnt_plus}{END}{cnt_plus*100/(cnt_minus+cnt_plus)}%\n-){BLUE}{" " * cnt_minus}{END}{cnt_minus*100/(cnt_minus+cnt_plus)}%")

zxc()