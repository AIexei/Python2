class My_xrange(object):
    def __init__(self, stop, start = 0, step = 1):
        self.stop = stop
        self.start = start
        self.step = step
        self.cur_value = start


    def __iter__(self):
        return self


    def __getitem__(self, item):
        return self.start + self.step * item


    def __len__(self):
        return int((self.stop - self.start) / self.step)


    def __str__(self):
        return 'xrange({0}, {1}, {2})'.format(self.stop, self.start, self.step)


    def __next__(self):
        if self.cur_value < self.stop:
            try:
                return self.cur_value
            finally:
                self.cur_value += self.step
        else:
            self.cur_value = self.start
            raise StopIteration















