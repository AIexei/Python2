def binary(value):
    x = 2**30
    result = ''

    while x >= 1:
        if (int(x) & int(value)) == x:
            result += '1'
        else:
            result += '0'

        x /= 2

    return result

def dec(string):
    bits = len(string)
    x = bits-1
    i = 0
    result = 0

    while x >= 0:
        if string[i] == '1':
            result += 2**x

        x -= 1
        i += 1

    return result

def func():
    print(2**10)


if __name__ == "__main__":
    func()