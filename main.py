def inverter(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return list(reversed(result))
    return wrapper

@inverter
def get_evens_nums(n: int) -> list:
    if n >= 0:
        return list(filter(lambda x: x % 2 == 0, range(0, n+1)))
    else:
        return list(filter(lambda x: x % 2 == 0, range(n, 0)))
print(get_evens_nums(10))