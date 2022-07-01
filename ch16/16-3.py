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

next(coro_avg)

print(coro_avg.send(10))  # 10 / 1 = 10
print(coro_avg.send(30))  # (10 + 30) / 2 = 20
print(coro_avg.send(5))  # (10 + 30 + 5) / 3 = 15
