from array import array
import reprlib
import math
import numbers


class Vector:
    typecode = "d"

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find("[") : -1]
        return "Vector({})".format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self._components)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = "{.__name__} indices must be integers"
            raise TypeError(msg.format(cls))

    # BEGIN VECTOR_V3_GETATTR
    # shortcut_names = "xyzt"

    # def __getattr__(self, name):
    #     cls = type(self)  # <1>
    #     if len(name) == 1:  # <2>
    #         pos = cls.shortcut_names.find(name)  # <3>
    #         if 0 <= pos < len(self._components):  # <4>
    #             return self._components[pos]
    #     msg = "{.__name__!r} object has no attribute {!r}"  # <5>
    #     raise AttributeError(msg.format(cls, name))

    # END VECTOR_V3_GETATTR

    # BEGIN VECTOR_V3_SETATTR
    # def __setattr__(self, name, value):
    #     cls = type(self)
    #     if len(name) == 1:  # <1>
    #         if name in cls.shortcut_names:  # <2>
    #             error = "readonly attribute {attr_name!r}"
    #         elif name.islower():  # <3>
    #             error = "can't set attributes 'a' to 'z' in {cls_name!r}"
    #         else:
    #             error = ""  # <4>
    #         if error:  # <5>
    #             msg = error.format(cls_name=cls.__name__, attr_name=name)
    #             raise AttributeError(msg)
    #     super().__setattr__(name, value)  # <6>

    # END VECTOR_V3_SETATTR

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


### 예제 getattr ###
v = Vector(range(10))

print(v)
# print(v.y, v.z, v.t, v.d)

# print(v.a)

### 예제 setattr ###
# v = Vector(range(5))
# print(v)

# print(v.x)
# v.x = 10
# print(v.x)

# print(v)
