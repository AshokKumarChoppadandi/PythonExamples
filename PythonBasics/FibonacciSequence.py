# Fibonacci Sequence

def print_fibonacci_series(number):
    print('PRINTING FIBONACCI SERIES TILL NUMBER : %d' % number)
    a, b = 0, 1
    while a <= number:
        print(a, " ", end="")
        temp = a
        a = b
        b = b + temp
    print('\nEnd of the program')


def main():
    number = int(input('Please enter a number :'))
    print_fibonacci_series(number)


if __name__ == '__main__':
    main()
