#input

"""num = input("숫자를 입력하세요!!")
print("number ", num)
"""

#type

"""a = 12
print(type(a))
a = 12.01
print(type(a))
a = "a"
print(type(a))
a = "abcd"
print(type(a))"""


#형변환

"""a = 65
# a = "65"
# print(int(a))
# print(str(a))
# print(hex(a))
# print(oct(a))
# print(chr(a))
print(ord("A"))"""

"""print(pow(2, 2))
print(pow(2, 6))
print(pow(3, 4))"""


#print(divmpd(10, 3))

# print(round(3.14))

""" a = (3, 5, 7)
b = list(a)
c = tuple(b)

print(a)
print(b)
print(c) """
 
 
#range

""" for i in range(2, 7):
    print(i) """

""" for i in range(6):
    print(i) """

""" for i in range(1, 20, 3):
    print(i) """



# max, min, sum

""" a = [3, 5, 6, 9]
print(max(a))
print(min(a))
print(sum(a)) """


# abs

"""print(abs(-3))
print(abs(3.0))
print(abs(-3.0))"""


# sorted

"""a = [5, 3, 1, 9, 4]
print(sorted(a))
print(sorted(a, reverse=True))"""


# enumerate

"""a = [5, 3.14, False, 9, "string"]
print(enumerate(a))
print(*enumerate(a))"""


# zip

a = [1, 2,3]
b = [4, 5, 6]
print(*zip(a,b))


# any, all

a = [True, True, False]
a = [True, True, True]
print(any(a))
print(all(a))
print(all(b))


# format

a = 20 
b = 23
c = "a는 {}, b는 {}".format(a, b, "python")

print(c)

a = 3
print(globals())
print(locals())

