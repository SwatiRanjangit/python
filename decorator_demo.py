#               DECORATOR
#-----------------------------------------------------------------------------

# it is a design pattern for any function allows user to add new functionality to existing function
# without making changes into it.


# DECORATOR FUNCTION EXAMPLE PROGRAM
def decor(f1):
    def inner(name):
        if name == 'durga':
            print("hello durga good evening")
        else:
            f1(name)
    return inner


@decor
def display(name):
    print("hello ", name," good morning")

display("sai")
display("swati")
display("durga")
