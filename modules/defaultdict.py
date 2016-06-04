class MyDefaultDict(dict):
    def __missing__(self, item):
        self[item] = MyDefaultDict()
        return self[item]


if __name__ == "__main__":
    a = MyDefaultDict()
    a[1][2][3] = 4
    print(a)



