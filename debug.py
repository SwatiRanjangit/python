#  DEBUGGING PYTHON PROGRAM USING ASSERT KEYWORD(Assertion)
# DEBUGGING: is the process of identifying the bug and fixing it
# assertion applicable for development time not production environment

# assert conditional_express,message  ---syntax

def square(n):
    return n*n

# DEBUG USINF PRINT() is problematic as it is output to the consol as well at the time of prpduction
# hence we go for assert to avoid this

# print("square of 3 should be 9")
# print("square of 4 should be 16")
# print("square of 5 should be 25")


assert square(3)==9,"square of 3 should be 9"
assert square(4)==16,"square of 4 should be 16"
assert square(5)==25, "square of 5 should be 25"
print(square(3))
print(square(4))
print(square(5))
