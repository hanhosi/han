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



# 사용가능 메소드

""" import calc
print(dir(calc)) """


# calc 모듈 호출

""" # res = calc,add(8, 4)
# pront(res)

print(calc.add(8, 4))
print(calc.sub(8, 4))
print(calc.mul(8, 4))
print(calc.div(8, 4)) """

"""import calc as cl

# res = calc,add(8, 4)
# pront(res)

print(cl.add(8, 4))
print(cl.sub(8, 4))
print(cl.mul(8, 4))
print(cl.div(8, 4))"""


# ciecle mod

""" import mod.circle_mod as cm

print(cm.pi)

print(cm.cc_area(4))
print(cm.cc_len(5)) """


# 문자열 자르기

""" def cusrt(st, wd, idx) :
    tmp = st.split(wd)
    res = tmp[idx]
    return res

url = "https://www.notion.so/test/4-1/a1fe5ef0df1/41f7a1aa9ec01/3a859a"
rs = cutstr(url, "/", 3) 
print(rs) """

# 문자유틸 모둘화

""" import mod.str_util as smod

url = "https://www.notion.so/test/4-1/a1fe5ef0df1/41f7a1aa9ec01/3a859a"
res = smod.cutstr(url, "/", 3)
print(res) """


# math 모듈 사용

""" import math

sq_res = math.sqart(6)
print(sq_res)

sp_res = math.sin(math.pi /2)
print(sp_res)

e_res = math.log(math.e)
print(e_res)

exp_res = math.exp(3)
print(exp_res)

pi_res = math.pi
print(pi_res)

math """



""" import mod.utils as mu

res = mu.mt_sqrt(7)
print(res)

sin = mu.mt_sinpi()
print(sin)

el = mu.mt_elog()
print(el)

ep = mu.mt_elog()
print(el)

ep = mu.mt_exp(3)
print(ep)

pi = mu.mt_pi()
print(pi) """



""" import random

# 1부터 10까지의정수 중에서 랜덤으로 선택
print(random.randint(1, 10))

# 리스트에서 랜덤으로 하나 선택
my_list = ['apple', 'banana', 'cherry']
print(random.choice(my_list))

# 0.0과 1.0 사이의 랜덤 실수 생성
print(random.random())

# 정규 분포물 따르는 랜덤 실수 생성
print(random.nprmalvariate(0, 1)) """



# 모듈화
"""import random as rd

res = rd.randint(1, 100)
print(res)

my_list = ["apple", "banana", "cherry"]
lres = rd.choice(my_list)
print(lres)

fres = rd.Random()
print(fres)

nvres = rd.normalvariate()
print(nvres)"""


""" # datetime 이용 함수
from datetime import datetime as dt

# 현재 시간 출력
# 특정 시간대의 현재 시간 출력
# from pytz import timezone
# import timezone
# tz = timezone('Asia/Seoul') """

""" 
# 문자열을 날짜로 변환
date_string = '2021-07-08'
date_object = dt.strptime(date_string, '%Y-%m-%d')
print(date_object)

# 날짜를 문자열로 변환
date_object = dt.now()
date_string = date_object.strftime('%Y-%m-%d')
print(date_string) """



""" import mod.utils as mu
# import datetime as dt

#print(dt.now()
dtnow = mu.get_dtnow()
print(dtnow)

ret = mu.cvt_time2str("2023-09-25")
print(ret)

res = mu.cvt_str2time()
print(res)
 """

""" # os 모듈 확인
import os

# 현재 작업 디렉토리 출력
print(os.getcwd())

# 디렉토리 변경
os.chdir('../')

# 변경된 디렉토리 출력
print(os.getcwd())

# 파일 목록 출력
print(os.listdir())

# 디렉토리 삭제
os.rmdir('new_directory')
print(os.listdir())

# 디렉토리 생성
os.mkdir('new_directory')
print(os.listdir()) """



""" import mod.utils as mu
import os

print(mu.get_curdir())

pnname = "python"
mu.os_mkdir(pnname)
print(os.listdir())

os.rmdir(pnname)
print(os.listdir()) """


import sys
print(sys.version)
print(sys.argv)