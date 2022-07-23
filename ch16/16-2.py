def simple_coro2(a):
    print("-> Started: a = ", a)
    b = yield a

    print("-> Started: b = ", b)
    c = yield a + b

    print("-> Started: c = ", c)


my_coro2 = simple_coro2(14)

from inspect import getgeneratorstate

print(getgeneratorstate(my_coro2))  # GEN_CREATED

next(my_coro2)
print(getgeneratorstate(my_coro2))  # GEN_SUSPENED

my_coro2.send(28)
print(getgeneratorstate(my_coro2))  # GEN_SUSPENED

try:
    my_coro2.send(99)  # StopIteration

except Exception as e:
    print(e)
    print(getgeneratorstate(my_coro2))  # GEN_CLOSED
