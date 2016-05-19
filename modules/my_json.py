class NotJsonSerializableException(TypeError):
    def __init__(self, value):
        self.value = value


    def __str__(self):
        return repr(self.value)


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
        raise NotJsonSerializableException(
            "Type {0} is not json serializable".format(type(obj)))

    return result

