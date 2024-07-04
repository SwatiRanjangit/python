from re import *

# MATCH OBJECT DEMO PROGRAM

# pattern = compile("ab")
# match = pattern.finditer("absabsabssbab")
#
# count=0
# for m in match:
#     count+=1
#     print(m.start(),"      ",m.end(),"      ",m.group())
#
# print("No of occurence of the matched string is: ",count)

# CHRACTER CLASS DEMO PROGRAM

# match = finditer("[abc]", "ab&tr%lkbbaxc")
# match = finditer("[^abc]", "ab&tr%lkbbaxc")
# match = finditer("[a-z]", "ab&tr%lkbbaxc")
# match = finditer("[A-Z]", "ab&tr%lANkbbaxc")
# match = finditer("[0-9]", "ab&tr%lkbbaxc")

#       Predefined Character class demo program

# match = finditer("\s", "ab&t r%lkb baxc")
# match = finditer("\S", "ab&t r%lkb baxc")
# match = finditer("\D", "ab&t r%lkb baxc")
# match = finditer("\d", "ab&t r%lkb baxc")
# match = finditer("\w", "ab&t r%lkb baxc")
# match = finditer("\W", "ab&t r%lkb baxc")

#           QUANTIFIERS DEMO PROGRAM

# match = finditer("a", "aaabbbbbaaabbababa")
# match = finditer("a+", "aaabbbbbaaabbababa")
# match = finditer("a*", "aaabbbbbaaabbababa")
# match = finditer("a?", "aaabbbbbaaabbababa")
# match = finditer("a{3}", "aaabbbbbaaabbababa")
# match = finditer("a{3,5}", "aaabbbbbaaaaabbababa")
#
#
# for m in match:
#     print(m.start(),"-------",m.group())


#===========================================================================

# p = input("Enter the pattern you wanna check: ")
# m = match(p,"durgasoft")
#
# if m != None:
#     print("pattern is found at the begning of the string")
# else:
#     print("pattern not found  at the begning of the string")


# p = input("Enter the pattern you wanna check: ")
# m = fullmatch(p,"durgasoft")
#
# if m != None:
#     print("pattern is found at the begning of the string")
# else:
#     print("pattern not found  at the begning of the string")



# p = input("Enter the pattern you wanna check: ")
# m = search(p,"durgasoft")
#
# if m != None:
#     print("pattern is found in string")
# else:
#     print("pattern not found in the string")

# p = input("Enter the pattern you wanna check: ")
# m = findall(p,"durgasoft is good and it is nice it is very good")
# print(m)

#
# l = sub("[a-z]","*","abc&*#^*(927FHfs")
# print(l)

# l = subn("[a-z]","*","abc&*#^*(927FHfs")
# print(l)

# l = split("\.","www.durgasoft.com")
# print(l)

s = "learning python is difficult GUYS"
# l = search("^learn",s)
#
# if l != None:
#     print("starts with learn ")
# else:
#     print("not starts with learn")



# l = search("guys$",s,IGNORECASE)
#
#
# if l != None:
#     print("ends with guys ")
# else:
#     print("not ends with guys")




