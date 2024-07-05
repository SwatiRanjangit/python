#               GENERATOR
#--------------------------------------------------------------------
# use to generate the large amount of value without any memory error
# memo error not occur cz at the begining it will not store all the value in memo hence we can
# generate large amount of number using it.
# we use it generally when we have huge number of database collection
# in generator yield is used instead of return it goesn't return any value either return interator of large values


# l = (x for x in range(10000000000000000000000000))
# print(type(l))
# for i in l:
#     print(i,end=" ")

# Gnerator function
def f1():
    yield 'hello'
    yield 'ho'
    yield 'helo'

# print(f1())
# for i  in f1():
#     print(i, end=" ")

g = f1()
print(next(g))
print(next(g))