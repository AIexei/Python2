import time

cache = dict()

def cached(function):
    def dec_function(arg):
       if arg in cache.keys():
            return cache.get(arg)
       else:
            result = function(arg)
            cache.update({arg: result})
            return result

    return dec_function


@cached
def fib(num):
    if num == 1 or num == 2:
        return 1
    return fib(num - 1) + fib(num - 2)


def bad_fib(num):
    if num == 1 or num == 2:
        return 1
    return bad_fib(num - 1) + bad_fib(num - 2)

def main():
    time.clock()

    start = time.clock()
    print(bad_fib(33))
    print("Exec time is %.5f \n" % (time.clock()-start))

    start = time.clock()
    print(fib(32))
    print("Exec time is %.5f " % (time.clock()-start))

    print('\n')
    print(cache)


if __name__ == "__main__":
    main()