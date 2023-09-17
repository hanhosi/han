"""x = [1, 2, 3]
y = [1, 2, 3]
z= x

print(x is y)
print(x is z)
print(x is not y)"""


"""a= 5
b =5

print(a is b)
print(a is not b)"""


"""a = 3
b = 3.0

print(a == b)
print(a is b)
print(a is not b)"""


"""a = [3 , 5, 1]
b = a

print(a is b)


a[0] = 2

print(a, b)

print(a is b)"""


#a = 2 + 3 * 4
#a = 10 / 5 / 2
#a = 2 ** 3 ** 2
#a = 2 ** (3 ** 2)
#a = 10 % 3 % 2
#a = 1 + 2 > 3 and 4 - 1 < 2
#a = not False and True
#a = not True or False and True
#a = 1 & 2 | 3 ^ 4
#a = 5 in [3, 4, 5] or 2 not in [1, 2, 3]
#a = 2 * -3 // 2
#a = 1 == 2 
#a = False != 3

#print(a)


"""#x = 0
#x =-1
x = 10

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")"""


# if 짝수, 홀수
"""num = 23
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")"""
    

"""a = 2
b = 2
if a == b:
    print("같습니다.")
else:
    print("다릅니다.")"""
    
    
"""char = "a"
if char == "a" or char == "b":
    print("'a' 또는 'b'입니다.")
else:
    print("'a' 또는 'b'가 아닙니다.")  """
    
    
    
"""fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)"""
    
    
# 이중 for 문 예시   
"""my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in my_list:
    for num in row:
        print(num)"""
        
        
# for 0 ~ 9 출력       
"""for i in range(10) :
    print(i)"""
    
# for 낱말 출력 
"""for char in "Python" :
    print(char)"""
    
    
# for 역순 출력 reversed
"""fruits = ["apple", "banana", "cherry"]"""
"""fruits = ["apple", "banana", "cherry"]

for fruit in reversed(fruits) :
    print(fruit)"""
    
# for 역순 출력 sorted
"""for fruit in sorted(fruits, reverse=True):
    print(fruit)"""
    
# for 구구단  
"""for i in range(1, 10):
    for j in range(1, 10):
        print(i, "x", j, "=", i*j)"""
        
# for else 예문
"""rng = [5, 8, 3, 1, 6]
for i in rng:
    print("element : ", i)
else :
    print("end process")"""
    

# 반복문 제어
"""for i in range(10):
    if i == 7:
        print("break ", i)
        break
    elif i == 1:
        print("continue ", i)
        continue
    else:
        print("pass ", i)
        pass

    print(i)"""
    
    
# while 1 ~ 5 출력
"""i = 1

while i <= 9:
    print(i)
    i += 1"""
    
    
# while 문자열 낱자 출력
"""str_word = "python"
idx = 0
 
while idx < len(str_word):
    print(str_word[idx])
    idx += 1"""


# while 1 ~ 10 종합
"""sum = 0
i = 1

while i <= 10:
    sum += i
    i += 1
    
print(sum)"""


# while 1 ~ 100 홀수, 짝수 출력
"""i = 1

while i <= 100:
    if i % 2 == 0:
        print("짝수 : ", i)
    elif i % 2 ==1:
        print("홀수 : ", i)
    i += 1"""
    

# while 7의 배수만 출력
i = 1

while i <= 100:
    if i % 7 == 0:
        print(i)
    i += 1





"""my_set = {1, 2, 3, 4, 5}
setItem = {5, 3, 1}
print(my_set)
print(setItem)"""

"""my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)

set_tmp = set("hello")
print(set_tmp)"""

"""my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}
print(my_set | set_item)"""

"""my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}
# print(my_set | set_item)
print(my_set.union(set_item))"""

"""my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}
print(my_set | set_item)
print(my_set - set_item)"""

"""my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}
print(my_set | set_item)
# print(my_set - set_item)
print(my_set.difference(set_item))"""

"""my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}
print(my_set | set_item)
print(my_set & set_item)"""

"""my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}
print(my_set | set_item)
# print(my_set & set_item)
print(my_set.intersection(set_item))"""

"""my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
my_set.add(9)
print(my_set)"""

"""my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
my_set.update([5, 9, 7, 4])
print(my_set)"""

"""my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
my_set.clear()"""

"""my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
my_set.remove(5)"""

"""my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
my_set.discard(2)
print(my_set)"""

"""my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}
print(my_set)
my_set.difference_update(set_item)
print(my_set)"""

"""my_int = 10
my_str = str(my_int)
print(my_int)
print(my_str)"""

"""my_int = 10
print(my_int)
print(my_int + 10)"""

"""my_int = 10
print(my_int)
print(my_int + 10)
my_str = str(my_int)
print(my_str)"""

"""my_int = 10
print(my_int)
print(my_int + 10)
my_str = str(my_int)
print(my_str)
print(my_str = 10)"""

"""my_int = 10
print(my_int)
print(my_int + 10)
my_str = str(my_int)
print(my_str)
print(my_str = "hello")"""

"""my_str = '10'
my_int = int(my_str)
print(my_str)
print(my_int)"""

"""my_str = '10'
print(my_str)
my_int = int(my_str)
print(my_int)
print(my_int + 10)"""

"""my_str = '10'
print(my_str)
my_int = int(my_str)
print(my_int)
print(my_int + 10)
my_int2 = int("ten")
print(my_int2)"""




"""x=10
y=3
print(x + y)    
print(x - y)    
print(x * y)    
print(x / y)    
print(x % y)    
print(x // y)   
print(x ** y)   """


"""a = 10
b = 3

a = 0
print(a)
a += 2
print(a)
a -= 1
print(a)
a *= 4
print(a)
a /= 2
print(a)
a **= 3
print(a)"""


"""x=10
y=4
print(x > y)    
print(x < y)    
print(x >= y)   
print(x <= y)   
print(x == y)   
print(x != y)   """


"""a = 10
b = 4

# c = a > b
# c = a < b
# c = a >= b
# c = a <= b
# c = a == b
c = (a != b)
print(c)"""


"""a = 1
b = 0 

print(a and b)
print(a or b)
print(not b)

x = True
y = False

print(x and y)
print(x or y)
print(not x)
print(not y)"""


"""a = 10
b = 3
# c = a & b
# c = a | b
# c = a ^ b
# c = a ~ b
c = a << 2
print(c)"""


my_list = [9, 4, 3, 7, 8, 'hi']
print(2 not in my_list)
my_dic = {"key1" : "v1", "k2" : "v2"}
print("k" in my_dic)