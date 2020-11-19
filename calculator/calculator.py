# Operations

# Add Operation
def add(x, y):
    return x + y

# Subtract


def sub(x, y):
    return x - y

# Multipy


def mult(x, y):
    return x * y

# Divide


def div(x, y):
    return x / y


# Choosing First Number

first_num = float(input('Enter The First Number :'))


# Choosing The Operation

opr = input('+ Or - Or / Or * :')


# Choosing The Second Number

second_num = float(input('Enter The Second Number :'))


# Calculing The Result
if opr in ('+', '/', '-', '*', 'X', 'x'):
    if opr == '+':
        res = add(first_num, second_num)
        print(f'{first_num} {opr} {second_num} = {res}')

    elif opr == '-':
        res = sub(first_num, second_num)
        print(f'{first_num} {opr} {second_num} = {res}')

    if opr in ('x', 'X', '*'):
        res = mult(first_num, second_num)
        print(f'{first_num} {opr} {second_num} = {res}')

    elif opr in ('/', '%'):
        res = div(first_num, second_num)
        print(f'{first_num} {opr} {second_num} = {res}')

else:
    print('Error: Invalid Input')

# GG
