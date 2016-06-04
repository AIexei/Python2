class Metaclass(type):
    def __new__(cls, name, bases, dct):
        file_name = "meta.txt"

        if "file_name" in dct:
            file_name = dct["file_name"]

        with open(file_name) as file:
            for line in file:
                if line != "":
                    attrs = line.strip().split(' ')
                    dct[attrs[0]] = attrs[1]
        return super(Metaclass, cls).__new__(cls, name, bases, dct)


class Temp(metaclass=Metaclass):
    pass


def main():
    t = Temp()
    print(t.x)
    print(t.y)
    print(t.z)


if __name__ == "__main__":
    main()