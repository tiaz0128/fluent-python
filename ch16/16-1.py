def simple_coroutine():
    print("-> coroutine started")

    x = yield

    print("-> coroutine recevied", x)


my_coro = simple_coroutine()
my_coro.send(42)

# next(my_coro)
# next(my_coro)
