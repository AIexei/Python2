class MyVector(object):
    def __init__(self, *args):
        self.vector = []

        for item in args:
            if isinstance(item, (int, float)):
                self.vector.append(item)
            elif isinstance(item, list):
                self.vector.extend(item)


    def __len__(self):
        return len(self.vector)


    def __getitem__(self, item):
        if item < len(self.vector):
            return self.vector[item]
        else:
            raise IndexError("Vector index out of range")


    def __str__(self):
        return str(self.vector)


    def __eq__(self, other):
        if isinstance(other, MyVector):
            return other.vector == self.vector
        else:
            return False


    def __mul__(self, mult):
        if isinstance(mult, (int, float)):
            temp = [mult * self[i] for i in range(len(self))]
            return MyVector(temp)
        elif isinstance(mult, MyVector):
            if len(self) == len(mult):
                return sum((self[i] * mult[i]) for i in range(len(self)))
            else:
                raise ValueError("Vector's len not equals!")


    def __add__(self, other):
        if isinstance(other, MyVector):
            if len(self) == len(other):
                result_vector = []

                for item in range(len(self)):
                    result_vector.append(self[item] + other[item])

                return MyVector(result_vector)
            else:
                raise ValueError("Vector's len not equals!")
        else:
            raise TypeError("Instances must be vectors!")


    def __sub__(self, other):
        if isinstance(other, MyVector):
            if len(self) == len(other):
                result_vector = []

                for item in range(len(self)):
                    result_vector.append(self[item] - other[item])

                return MyVector(result_vector)
            else:
                raise ValueError("Vector's len not equals!")
        else:
            raise TypeError("Instances must be vectors!")


    def append(self, value):
        if isinstance(value, (int, float)):
            self.vector.append(value)
        else:
            raise TypeError("Value have wrong type")


def main():
    a = MyVector(1, 2, 3, 4, 5)
    b = MyVector(9, 8, 7, 6, 5)

    print(a * b)
    print()

    a = a - b
    print(a)
    print(b)
    print()

    b = b * 3
    print(a)
    print(b)
    print()

    print(a == b)

if __name__ == "__main__":
    main()




