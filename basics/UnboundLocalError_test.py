x = 10


def bar():
    nonlocal x
    print(x)
    x += 1


bar()
