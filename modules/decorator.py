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