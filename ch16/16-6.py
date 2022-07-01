from functools import wraps

# 클로저 func
def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)  # 코루틴 생성
        next(gen)  # 코루틴 가동
        return gen

    return primer


@coroutine
def averager():
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


coro_avg = averager()

from inspect import getgeneratorstate

print(getgeneratorstate(coro_avg))  # GEN_SUSPENDED

print(coro_avg.send(10))
try:
    print(coro_avg.send("spem"))
except Exception:
    pass
print(coro_avg.send(5))  # StopIteration
