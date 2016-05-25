class MyDefaultDict(dict):
    def __missing__(self, item):
        self[item] = MyDefaultDict()
        return self[item]


def main():
    a = MyDefaultDict()
    a[1][2][3] = 4
    print(a)

if __name__ == "__main__":
    main()



