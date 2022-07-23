MyClass = type("MyClass", (object,), {"x": 42, "x2": lambda self: self.x * 2})
print(MyClass)

my = MyClass()
print(my.x)
print(my.x2())

# o1 = type('X', (object,), dict(a='Foo', b=12))
# print(type(o1))

# print(vars(o1))

# class test:
#   a = 'Foo'
#   b = 12

# o2 = type('Y', (test,), dict(a='Foo', b=12))
# print(type(o2))
# print(vars(o2))
