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

"""a = [1, 2,3]
b = [4, 5, 6]
print(*zip(a,b))"""


# any, all

"""a = [True, True, False]
a = [True, True, True]
print(any(a))
print(all(a))
print(all(b))
"""


# format

"""a = 20 
b = 23
c = "a는 {}, b는 {}".format(a, b, "python")

print(c)"""

"""a = 3
# print(globals())
# print(locals())"""

"""print(dir(a))

print(callable(a))"""


#lambda

""" add = lambda a, b : a + b
print(add(2, 3))


add = lambda a, b : a + b
sub = lambda a, b : a - b
mul = lambda a, b : a * b
div = lambda a, b : a / b

print(add(2, 3))
print(sub(2, 3))
print(mul(2, 3))
print(div(2, 3)) """


# 사용자 정의

"""def add_numbers(x, y):
    return x + y

# 함수 호출
result = add_numbers(4, 5)
print(result)"""


"""def greet(name):
    print(name)
    
    print("Hello, " + name + ". How are you?")

greet("최서연")"""


# 매개변수, 인자

""" def add(a, b) : 
	print(a + b)

def sub(a, b) :
	return a - b

def mul() :
	return 2 * 4

def div() :
	print(4 / 2)

add(3, 5)
print(sub(3, 5))
print(mul())
div() """


# 입력값 홀/짝수

""" def is_even(n) :
    if  n % 2 == 0:
        print("짝수")
    else :
        print("홀수")
        
num = input("숫자를 입력하세요 : ")

is_even(int(num)) """


# 문자열 반전

""" def reverse_string(msg) :
    return msg[::-1]

in_str = input("문자열 : ")
print(reverse_string(in_str))


# 두수를 입력받아 사칙연산

def add(a, b) :
    return int(a) + int(b)
def sub(a, b) :
    return int(a) - int(b)
def mul(a, b) :
    return int(a) * int(b)
def div(a, b) :
    return int(a) / int(b)

a = input("a를 입력하세요")
b = input("b를 입력하세요")

print("더하기 : ", add(a, b))
print("삐기 : ", sub(a, b))
print("곱하기 : ", mul(a, b))
print("나누기 : ", div(a, b))


def calc(a, b) :
    print(int(a) + int(b))
    print(int(a) - int(b))
    print(int(a) * int(b))
    print(int(a) / int(b))
    
a = input("a를 입력하세요")
b = input("b를 입력하세요")

calc(a, b) """



# 5개 수 입력 
""" def sum_num(num) :
    return sum(num)

nums = []

for i in range(1, 6) :
    innum = int(input(f"{i} 번쨰 숫자 입력 : "))
    
print(sum_num(nums))  """



# 콜백함수

""" def prt_func() :
    print("hello")

def callfunc(fx) :
		fx()

callfunc(prt_func)  """

""" def prt_func(n) :
    print("hello", n)

def callfunc(fx) :
    for i in range(5) :
	    fx(i)

callfunc(prt_func) """



# 타입힌트 -콜백함수

""" def update_msg(name: str) -> list:
    msg = []
    msg.append("Hello, " + name)
    msg.append("Bye, " + name)
    return msg
    
def greeting(in_name: str) -> list:
    gt_msg = None
    gt_msg = update_msg(in_name)
    return gt_msg
res = greeting("python")

for message in res:
    print(message) """
    
    
""" def fun(n) :
    if n == 5 :
        return
    
    print(1, n)
    fun(n+1)
    
fun(1) """


""" def ploop(n) :
    if n ==0:
        print("end")
        return 1
    else : 
        print(n, n-1, " = ", n + n-1)
        return n * ploop(n-1)
    
print(ploop(3)) """


""" def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print(n)
        return fibonacci(n-1) + fibonacci(n-2)
    
res = fibonacci(4)
print("res = ", res) """