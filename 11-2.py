# 변환

import pandas as pd

df = pd.read_csv("./data/apttt.cvs", index_col=0)
# print(df.head())

""" df = df.rename(columns={"분양가격(제곱미터)":"분양가"})
# print(df.head())
# print(df.dtypes)

df["분양가"] = df["분양가"].convert_dtypes()
# print(df.dtypes)
print("\n------------------\n") """


# 정렬

res = df.sort_values(by="지역명, ascending=True")
res = df.sort_values(by="지역명, ascending=False")
print(res.head(10))
print(res.head(5))

# res = df.sort_values(by="연도")
# res = df.sort_values(by="분양가")
res = df.sort_values(by="연도")[10:20]
# print(res)
# print(res.head())



# 컬럼 이름 출력

""" res = df["지역명"][:5]
# res = df[["지역명", "연도"]]
# res = df[["지역명", "연도", "분양가"]]
# res = df[["지역명", "연도", "분양가"]][:7]
# res = df["지역명", "연도"][:5]
# print(res)

res = df.loc[df["지역명", "연도", "분양가"]][:5]
# res = df.loc[:][:5]
# res = df.loc[:][:]
# res = df.loc[1]
# print(res)

res = df.loc[:6, ["지역명", "연도"]]
# res = df.loc[:6, ["지역명", "연도"]][:3]
# res = df.loc[:6, ["지역명", "연도"]][3:]
# res = df.loc[:6, ["지역명", "연도"]][:7]
# print(res) """



# 필터 출력

""" res = df.loc[df["지역명"]=="강원"]
# res = df.loc[df["연도"] > 2020]
# res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]]
# res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]][:10]
# res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]][-10:]
print(res) """



# 인덱스 지정 선택

df0 = df.copy()
print(df0)

# res = df.iloc[2]
res = df.iloc[2][2]
print(res)
