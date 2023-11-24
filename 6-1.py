# 미니 프로젝트

""" for i in range(5, 0, -1):
    for j in range(i):
        print('*', end='')
    print()  """


# (1) 직각삼각형

""" for i in range(1, 6):
    print("*" * i) """



""" # 역직각삼각형

for i in range(5, 0, -1):
    print("*" * 1) """
    
    
    
 # (2) 이등변 삼각형
 
""" for i in range(1, 6):
     spaces = "" * (6 -i)
     stars = "*" * (2 * i - 1)
     print(spaces + stars) """
     
     
     
# (3) n = 5 # 삼각형의 높이를 설정

""" for i in range(6, 0, -1):
    spaces = "" * (6 - i)
    stars = "*" * (2 * i -1)
    print(spaces + stars)    """
    
     
     
# 5 X 5 출력

""" num = 0
line = []
for i in range(5):
    for j in range(5):
        num += 1
        line.append(num)
    print(line)
    line = [] """
    
    
    
# 세로로 출력

""" line = []
for i in range(1, 6):
    for j in range(1, 6):
        num = ((j - 1) * 5) + i
        line.append(num)
        print(line)
        line = [] """
        
        

# 역순 출력

""" num = 26
line = []
for i in range(5):
    for j in range(5):
        num = 1
        line.append(num)
        # print(line)
    print(line)
    line = [] """
    
    
    
""" import random

sel = ['가위', '바위', '보']
result = {0 : '승리했습니다.', 1: '패배했습니다.', 2: '비겼습니다.'}

def chechkwin(user, com) :
    
    if not user in sel :
        print('잘못 입력하였습니다. 다시 입력하세요')
        return False
    print(f'사용자 ({user} vs {com} ) 컴퓨터')
    if user == com :
        state = 2
    elif user == '가위' and com == '바위' :
        state = 1
    elif user == '바위' and com == '보' :
        state = 1
    elif user == '보' and com == '가위' :
        state = 1
    else :
        state = 0
    print(result[state])
    return True """