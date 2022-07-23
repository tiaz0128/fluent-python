# 하위 코루틴
def accumulate():
    total = 0
    while True:
        x = yield
        if x is None:  # 받아온 값이 None이면
            return total  # 합계 total을 반환
        total += x


# 상위 코루틴
def sum_coroutine():
    while True:
        total = yield from accumulate()  # accumulate의 반환값을 가져옴
        print(total)


co = sum_coroutine()
next(co)

for i in range(1, 11):  # 1부터 10까지 반복
    co.send(i)
co.send(None)

for i in range(1, 101):  # 1부터 100까지 반복
    co.send(i)
co.send(None)
