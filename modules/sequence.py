class Sequence(object):
    def __init__(self, iterable):
        if hasattr(iterable, '__iter__'):
            self.items = iterable
        else:
            raise TypeError('Iterable object expected!')

        self.filter = None


    def __iter__(self):
        return self.items.__iter__()


    def __len__(self):
        return len(self.items)


    def __str__(self):
        return str(self.items)


    def filtrate(self, function):
        if self.filter != function:
            print('yes')
            dx = 0

            for i in range(len(self.items)):
                temp = self.items[i-dx]

                if not function(temp):
                    self.items.remove(temp)
                    dx += 1

            self.filter = function





