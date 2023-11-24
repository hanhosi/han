# 파일 생성

""" from faker import Faker as fk
import os

temp = fk("ko-KR")
print(temp.name())

folder = "data/"
if not os.path.isdir(folder) :
    os.mkdir(folder)
    
with open(folder + "fktemp.csv", "w", encoding='utf8') as f :
    f.write("name,address,postcode,company,job,phone,email,id,ip_prv,ip_pub,catch_parase,color\n")

with open(folder + "fktemp.csv", "a", newline='', encoding='utf8') as f :
    for i in range(30) :	
     f.write(temp.name() + "," + 
            temp.address() + "," + 
            temp.postcode() + "," + 
            temp.company() + "," + 
            temp.job() + "," + 
            temp.phone_number() + "," + 
            temp.email() + "," + 
            temp.user_name() + "," + 
            temp.ipv4_private() + "," + 
            temp.ipv4_public() + "," + 
            temp.catch_phrase() + "," + 
            temp.color_name() + "\n") """

import pandas as df
import pandas as pd

# rank 매기기

""" df["aver"] = df.postcode.rank(method="average")
# print(df[["postcode", "aver"]])

df["dense"] = df.postcode.rank(methos="dense")
# print(df[["postcode", "dense"]])

df["first"] = df.postcode.rank(methos="first")
# print(df[["postcode", "first"]])

df["min"] = df.postcode.rank(methos="min")
# print(df[["postcode", "min"]])

df["max"] = df.postcode.rank(methos="max", ascending=False)
# print(df[["postcode", "max"]])

print(df[["postcode", "max", "min", "first", "dense", "aver"]]) """



# 전치 컬럼-로우 변환

""" print(df.transpose) """



# 누적 계산

""" df["postcode"].expanding().sum()
print(df["postcode"].expanding().max()) """


# 내림차순 기준

""" print(df.postcode.idxmax(axis=0))   # 가장 작은수

print(df.postcode.idxmin(axis=0))   # 가장 큰수 """



# empty 추가

""" # print(df.empty)
print(df.case.empty) """



# 인자 검색

""" print(df.isin[48742])
print(df.isin["장상호"])

print(df.isin([48742, 12834]))

print(df.isin([48742, 12834, "장상호"]))
 """


# 기간 계산

""" # period = pd.period_range(start="2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq="30T")
period = pd.period_range(start="2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq="30T")
dt = {"col1":[1,2,3,4,5,6],"col2":period}
idx = ["row1","row2","row3","row4","row5","row6"]
pf = pd.DataFrame(data=dt, index=idx)
print(pf) """



# 인덱스 시간 - 간격 생성

""" # i = pd.date_range("2023-11-10", periods=10, freq="1H")
i = pd.date_range("2023-11-10", periods=10, freq="3H")
df = pd.DataFrame({"col1":[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df) """


# print("\n------------------\n")



# 특정시간 찾기

""" print(df.at_time("00:00"))
print(df.at_time("03:00")) """


# 범위 찾기

""" #print(print(df.between_time(start_time="12:00", end_time="00:00")))

print(print(df.between_time(start_time="03:00", end_time="09:00"))) """




# x일 간격 생성 - 기간별 찾기

""" i = pd.date_range("2023-11-10", periods=10, freq="3D")
# i = pd.date_range("2023-11-10", periods=10, freq="5D")
df = pd.DataFrame({'col1':[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)

# print(df.first("3D"))

print(df.first("7D"))

print(df.last("7D")) """




# pip install Finance-DataReader
import FinanceDateReader as fdr