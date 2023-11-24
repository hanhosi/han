# dataframe

""" import pandas as pd

df = pd.DataFrame([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]])
print(df)
print("\n------------------\n")

print(df[1])
print("\n------------------\n")

print(df[1][1])
print("\n------------------\n") """




# dataframe 출력

""" import pandas as pd

data = {
    "x" : [10, 15, 20],
    "y" : [50, 55, 60],
    "z" : [100, 110, 120]
}

idx = ["x축", "y축", "z축"]

fr = pd.DataFrame(data, index=idx)

print(fr)
print("\n------------------\n")

#print(fr["x"])
# print(fr["z"])

# print(fr. x)
# print("\n------------------\n")
# print(fr. y)

print(fr.ilo[1])

# print("\n------------------\n")
# print(fr.loc["y축"])

# print("\n------------------\n") """



# 열 추가

f""" rs = pd.DataFrame(fr, columns=["x", "y", "z", "t"])
print(frs)
print("\n------------------\n")

frs["t"] = [60, 120, 180]
print(frs)
print("\n------------------\n")


# 행 추가

frs.loc["t축"] = [100, 200, 300, 400]
# frs.loc["t축"] = [100, 200, 300]
print(frs)


# 행 수정
print("\n------------------\n")
frs.loc["t축"] = [500, 600, 700, 800]
print(frs)


#행 삭제
print("\n------------------\n")
# frs.drop("x", axis=1, inplace=True)
frs.drop("x축", axis=0, inplace=True)
print(frs)


# 열 삭제
print("\n------------------\n")
frs.drop("x축", inplace=True)
print(frs) """



# 컬럼 추가

""" import pandas as pd

dt = [[1,10,100],[2,20,200],[3,30,300]]
col = ["x","y","z"]
idx = ["x축","y축","z축"]

col = ["col1", "col2", "col3"]
idx = ["row1", "row2", "row3"]

df = pd.DataFrame(data=dt,index=idx,columns=col)

print(df)
# print(df["col1"])
# print(df["x"])
# print(df["y"])

print("\n------------------\n")
print(df.loc["row2"])
# print(df.loc["x축"])
# print(df.loc["y축"])

# print(df["col1"])

# print(df + 1)

# print(df.div(100))
# print(df / 100)
# print("\n------------------\n")

# print(df.mul(100))
# print(df * 100) """



""" import pandas as pd

dt = [[1, 10, 100], [2, 20, 200], [3, 30, 300]]
col = ["col1", "col2", "col3"]
idx = ["삼성", "현대", "LG"]

df = pd.DataFrame(data=dt, index=idx, colums=col)

print(df)
# print(df["col1"])
# print(df["y"])

print("\n------------------\n")
print(dt.loc["현대"])
# print(df.loc["y축"])

# print(df["col1"])

print("\n------------------\n")
print(dt + 1) """



# 같은 인덱스끼리 연산

""" dt2  = [[0],[2],[3]]
df2 = pd.DataFrame(data=dt2,index=["삼성", "현대", "LG"],columns=["y"])

print(df2)

print("\n------------------\n")
# print(df.div(df2))
print(df.div(df2))

print("\n------------------\n")
print(df.div(df2, fill_value=100)) """



# 멀티 인덱싱

""" import pandas as pd

idx = [('row1', 'val1'), ('row1', 'val2'), ('row2', 'val1'), ('row2', 'val2'), ('row2', 'val3'), ('row3', 'val2'),('row3', 'val3')]
dt = [ [1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18], [19,20,21]]

ind = pd.MultiIndex.from_tuples(idx)
df = pd.DataFrame(dt, columns=['col1', 'col2', 'col3'], index = ind)

print(df)

print("\n------------------\n")
# print(df.loc["row1=3"])
print(df.loc[0])

print("\n------------------\n")
print(df.loc[("row2", "val3")])

print("\n------------------\n")
print(df.loc[("row3", "val3"), "col1"])

print("\n------------------\n")
print(df.iloc[1][2]) """



# 랜덤 데이터 생성

""" import pandas as pd
import numpy as np

dt = np.random.randint(10, size=(5, 5))
df = pd.DataFrame(dt)

print(df)

print("\n------------------\n")
print(df[2])

print("\n------------------\n")
print(df[3][1])

print("\n------------------\n")
print(df.head(3))

print("\n------------------\n")
print(df.tail(2))

print("\n------------------\n")
print(df.sample())

print("\n------------------\n")
print(df.sample(3)) """