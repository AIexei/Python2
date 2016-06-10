import json
import re


class NotJsonSerializableException(TypeError):
    def __init__(self, obj):
        print("Type {0} is not json serializable".format(type(obj)))


def to_json(obj, raise_unknown = False):
    result = ''

    if isinstance(obj, bool):
        if obj:
            result += 'true'
        else:
            result += 'false'
    elif isinstance(obj, (int, float)):
        result += str(obj)
    elif isinstance(obj, (list, tuple)):
        result += '['

        for item in obj:
            result += to_json(item)
            result += ', '

        result = result[:-2] + ']'
    elif isinstance(obj, dict):
        result += '{'

        for item in obj.items():
            result += to_json(item[0]) + ': ' + to_json(item[1])
            result += ', '

        result = result[:-2] + '}'
    elif isinstance(obj, str):
        obj = obj.replace('\\', '\\\\')
        obj = obj.replace('\n', '\\n')
        obj = obj.replace('\"', '\\"')
        obj = obj.replace('\t', '\\t')

        result += '\"' + obj + '\"'
    elif obj is None:
        result += 'null'

    if raise_unknown is True:
        raise NotJsonSerializableException(obj)

    return result


def from_json(line):
    def parse_list(line):
        obj = []
        temp = []

        line = line.strip()[1:-1]
        values = line.split(', ')

        for i in range(len(values)):
            if i >= len(values):
                break
            if values[i].startswith('{') or values[i].startswith('['):
                symbol = ''

                if values[i].startswith('{'):
                    symbol = '}'
                else:
                    symbol = ']'

                d = ''

                while not values[i].endswith(symbol):
                    d += values[i]
                    d += ', '

                    values.remove(values[i])

                d += values[i]
                values.remove(values[i])

                temp.append(d)
            else:
                temp.append(values[i])

        for i in temp:
            obj.append(from_json(i))

        return obj

    def parse_dict(line):
        obj = {}
        line = line.strip()[1: -1]
        values = line.split(', ')

        for i in values:
            temp = i.split(': ')
            obj.update({from_json(temp[0]): from_json(temp[1])})

        return obj

    line = line.strip()

    if re.match('\[.*\]', line):
        obj = parse_list(line)
    elif re.match('\{.*\}', line):
        obj = parse_dict(line)
    elif re.match('\".*\"', line):
        obj = line[1:-1]
    elif re.match('-?\d+\.\d+', line):
        obj = float(line)
    elif re.match('-?\d+', line):
        obj = int(line)
    elif re.match('null', line):
        obj = None
    elif re.match('true|false', line):
        if line == "true":
            obj = True
        else:
            obj = False
    else:
        raise TypeError("JSON line is not valid")
    return obj


def main():
    # print(json.dumps(['\\\tf\\oo\n', {'bar': ('baz', None, 1.0, 2)}]))
    # print(to_json(['\\\tf\\oo\n', {'bar': ('baz', None, 1.0, 2)}]))
    # print('\n')

    # print(from_json("{false: true}"))
    print(from_json("[1.123, {2: false, 1: \"amma\"}, 4, null, [1, false, [\"1.23341\", 2]]]"))


if __name__ == "__main__":
    main()