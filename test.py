import convert

f = open("test.py", "r")
print(convert.from_python(f.read()))


class Test:
    pass
