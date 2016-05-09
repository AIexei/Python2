class My_vector(object):
    def __init__(self, *args):
        self.vector = []

        for item in args:
            if isinstance(item, (int, float)):
                self.vector.append(item)


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
        if isinstance(other, My_vector):
            return other.vector == self.vector
        else:
            return False


    def __mul__(self, mult):
        if isinstance(mult, (int, float)):
            temp = [mult * self[i] for i in range(len(self))]
            result = My_vector()

            for i in range(len(self)):
                result.append(temp[i])

            return result
        elif isinstance(mult, My_vector):
            if len(self) == len(mult):
                temp = [mult[i] *self[i] for i in range(len(self))]
                result = My_vector()

                for i in range(len(self)):
                    result.append(temp[i])

                return result
            else:
                raise ValueError("Vector's len not equals!")


    def __add__(self, other):
        if isinstance(other, My_vector):
            if len(self) == len(other):
                result_vector = []

                for item in range(len(self)):
                    result_vector.append(self[item] + other[item])

                self.vector = result_vector
                return self
            else:
                raise ValueError("Vector's len not equals!")
        else:
            raise TypeError("Instances must be vectors!")


    def __sub__(self, other):
        if isinstance(other, My_vector):
            if len(self) == len(other):
                result_vector = []

                for item in range(len(self)):
                    result_vector.append(self[item] - other[item])

                self.vector = result_vector
                return self
            else:
                raise ValueError("Vector's len not equals!")
        else:
            raise TypeError("Instances must be vectors!")


    def append(self, value):
        if isinstance(value, (int, float)):
            self.vector.append(value)
        else:
            raise TypeError("Value have wrong type")




