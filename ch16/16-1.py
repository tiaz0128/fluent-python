def simple_coroutine():
    print("-> coroutine started")

    x = yield

    print("-> coroutine recevied", x)


my_coro = simple_coroutine()

# next(my_coro)
my_coro.send(42)
