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
# match = finditer("\s", "ab&t r%lkb baxc")
# match = finditer("\S", "ab&t r%lkb baxc")
# match = finditer("\D", "ab&t r%lkb baxc")
# match = finditer("\d", "ab&t r%lkb baxc")
# match = finditer("\w", "ab&t r%lkb baxc")
# match = finditer("\W", "ab&t r%lkb baxc")
# match = finditer("a", "aaabbbbbaaabbababa")
# match = finditer("a+", "aaabbbbbaaabbababa")
# match = finditer("a*", "aaabbbbbaaabbababa")
# match = finditer("a?", "aaabbbbbaaabbababa")
# match = finditer("a{3}", "aaabbbbbaaabbababa")
match = finditer("a{3,5}", "aaabbbbbaaaaabbababa")


for m in match:
    print(m.start(),"-------",m.group())

