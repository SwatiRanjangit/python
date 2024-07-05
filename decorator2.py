
def swapNumbers(divide):
    def inner(a,b):
        if a < b:
            a,b = b,a
            return divide(a,b)
    return inner

@swapNumbers
def divide(a,b):
    print(a/b)

divide(2,4)