class Logger(object):
    def __init__(self):
        self.__logs__ = []


    def __getattribute__(self, attr):
        return 0


    def __str__(self):
        #return '\n'.join([
        #    'Name: {0}. Args: {1} {2}. Result: {3}\n'.format(name, args, kwargs, result)
        #    for name, args, kwargs, result if self.__logs__
        #])
        return 0

    

