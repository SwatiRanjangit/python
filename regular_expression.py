#                       REGULAR EXPRESSION
#-----------------------------------------------------------------------------

# it is a declarative mechnaism of which is used represent group of string according to the
# perticular pattern
# used for Validations: process of checking entered values are correct or not
# to use it we should import re module
# \d{10}: digits should be of 10 numbers only
# \w{10}: words should be of 10 letters only

# re module functions:

# 1. compile(): use to compile a pattern into regex object
# 2. finditer(): use to find iteration of match object

# ON MATCH METHODS WE CAN APPLY THESE METHODS:
# 1. start(): return start index of the match
# 2. end(): return end+1 index of the match
# 3. group(): return the matched string

# 3.







#======================= CHARATCTER CLASSES ===============================
# we use character classes  to search a group of characters
# syntax: [abc] : either a or b or c
#         [^abc] : except a , b , and c
#         [a-z] : any lower alphabet symbol
#         [A-Z] : any upper alphabet symbol
#         [0-9] : any digit from 0 to 9
#         [0-9a-zA-Z] : any alphanumeric
#         [^0-9a-zA-Z] : except  alphanumeric(special symbol)


#       Predefined Character class:
# \s : space character
# \S: any charcter excpt space character
# \d : any digit from 0-9
# \D : any character except digits
# \w : any word character [a-zA-Z0-9]
# \W : any word character except [a-zA-Z0-9]


#                   QUANTIFIERS
#=====================================================================
# we use to specify number of occurence to match
# a : exactly one 'a'
# a+ : atleast one a
# a* : any  number of a including 0 number of a
# a? : at most one a either 0 or 1 a
# a{m} : exaclty m number of a
# a{m,n} : minimum m number of a and maximum n number of a
