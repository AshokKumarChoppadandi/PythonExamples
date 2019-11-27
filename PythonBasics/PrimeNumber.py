print('Hello')


def is_prime(num):
    count = 0
    for x in range(2, num + 1):
        if num % x == 0:
            count += 1

    if count > 1:
        return False
    else:
        return True


def main():
    number = int(input('Please enter a number : '))
    res = is_prime(number)
    print(number, "is a prime number :", res)


if __name__ == '__main__':
    main()
