def log(f):
    def wrapper(*args, **kwargs):
        print("call %s:" % f.__name__)
        return f(args[0], args[1])

    return wrapper


@log                    # 装饰字   add = log(add)
def add(x, y):
    return x + y


@log
def sub(x, y):
    return x - y


print(add(3, 2))
print(sub(3, 2))



