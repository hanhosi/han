""" for i in range(5, 0, -1):
    for j in range(i):
        print('*', end='')
    print()  """


# 직각삼각형

""" for i in range(1, 6):
    print("*" * i) """



""" # 역직각삼각형

for i in range(5, 0, -1):
    print("*" * 1) """
    
    
    
 # 이등변 삼각형
 
""" for i in range(1, 6):
     spaces = "" * (6 -i)
     stars = "*" * (2 * i - 1)
     print(spaces + stars) """
     
     
     
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

num = 26
line = []
for i in range(5):
    for j in range(5):
        num = 1
        line.append(num)
        # print(line)
    print(line)
    line = []
    
    
    
    
    
    
    
    
    
# readlines 읽기

f = open("temp.txt", "r")
line = f.readlines()
for i in line :
    print(1)
    
f.close()

# file objedt

f = open