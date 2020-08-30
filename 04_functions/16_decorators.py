def div(a, b):
    print(a/b)


def smart_div(func):
    def inner_fun(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner_fun


div = smart_div(div)
div(2, 4)
