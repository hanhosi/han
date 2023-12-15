import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd
import FinanceDataReader as fdr 



# 다중 그래프 출력

x1 =[2, 3, 6, 7, 10]
x2 = [1, 4, 5, 8, 9]
x1 = [1, 4, 5, 8, 9]
x2 = [2, 4, 6, 8, 10]

y1 =[2, 3, 6, 7, 10]
y2 = [1, 4, 5, 8, 9]
y1 = [1, 4, 5, 8, 9]
y2 = [2, 4, 6, 8, 10]


# plt.subplot (2, 1, 1)
# plt.subplot (1, 2, 2)
# pit.subplot (3, 1, 1)
# pIt.subplot (2, 2, 1) 
plt.plot (x1, y1, "o-")


plt. subplot (2, 1, 2) 
plt. plot (x2, y2, ".-")

plt. subplot (2, 1, 1)
plt. subplot (1, 2, 2)
plt. subplot (3, 1, 1)
plt.plot (x1, y1, "o-")
plt. plot (x2, y2, ".-")

plt. title("X1 Graph")
plt.xlabel ("x1-data")
plt.ylabel ("y1-data")

plt.title("X2 Graph")
plt.xlabel ("x2-data")
plt.ylabel ("y2-data")

plt.title("X3 Graph")
plt.xlabel ("x3-data")
plt.ylabel("y3-data")

plt. title ("X4 Graph")
plt.xlabel ("x4-data")
plt. ylabel ("y4-data")




# 스타일 저장

plt.style.use("Soraize_Light")
plt. tight_layout()




# 이미지 저장

plt.savefig ("deta/img.jpg")
plt.savefig("deta/img -png")


x_years = ["2020", "2021", "2022" ]
y_data = [100, 400, 900]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
#ax1. bar (x_years, y_data)
#ax2. bar (x_years, y_data)
#ax3. bar (x_years, y_data)
#ax4. bar (x_years, y_data)

ax1.bar (x_years, y_data, color="aqimarine", edgecolor="black", hatch="/")
ax2.bar (x_years, y_data, color="saimon", edgecolor="black", hatch="\\") 
ax3.bar (x_years, y_data, color="navajowhite", edgecolor="black", hatch="+") 
ax4.bar (x_years, y_data, color="lightskyblue", edgecolor="black", hatch="*")

plt.tight_layout()

plt. show ()



# 데이터 처리 활용용

# seaborn 상관관계

# pip install plotly

""" tips = sns.load_dataset ("tips")
print (tips)

sns.regplot(x="total_bi11", y="tip", data=tips)

plt.show() """


""" tips = sns. load_dataset ("tips")
print (tips)

#plt. figure (figsize=(10.0))

sns.regplot(x="day", y="tip", data=tips)
#sns. barplot (×="day", y="total_bill", data=tips, palette="viridis")
#sns.barplot （x="tip"， y="total_bill"， data=tips）
#sns.barplot（x="sex"， y="total_bill"， data=tips）
#sns.barplot（x="sex"， y="tip"， data=tips）
#sns.barplot（x="smoker"， y="tip"， data=tips）
#sns.barplot（x="smoker"， y="rotal_bill"， data=tips）
#sns.barplot（x="time"， y="total_bill"， data=tips）

plt.title("Average Tips0")
plt.xlabel ("x")
plt. ylabel ("average")

plt. show() """



# 타이타닉 예제

""" titanic = sns.load_dataset("titanic")

sns.barplot(x="sex", y=" survived", hue="pclass", data=titanic)
plt. show()
#각 지표별 출력 
"titanic = sns, load_dataset("titanio")
print (titanic)

#sns. countplot(×="class", hue="who", data=titanic) 
sns. countplot (×="class", hue="alive", data=titanic) #sns. countplot(×="sex", hue="alive", data=titanic) 
#sns. countplot (×="alone", hue="who", data=titanic)

#sns. barplot(x="embark_town", y="survived", hue="pclass", data=titanic)
#sns. barplot(x="sex", y="survived", hue="pclass", data=titanic)

plt. show() """



# 주식 데이터 분석

""" df = fdr.DataReader ("KS11" )
df0 = df.loc["2023"]

print (df0)

# df0[ "Open" ], plot()
# df0[ "High" ], plot()
# df0[ "Low"], plot ()
# df0[ "Close"], plot ()

plt.grid(True)
plt. show()  """




# 다우지수와 코스피 비교

""" dow = fdr. DataReader ("DJI", "2010-06-01" )
kospi = fdr. DataReader ("KS11", "2010-06-01")


# plt.ftgure(tigsize=(7, 7))

# 각 지수별 종가 기준 그래프 출력
plt.plot (dow.index, dow.Close, "r--", label="Dow") 
plt. plot (kospi.index, kospi.Close, "b", label="KOSPI")



# 최고가 기준
plt.plot (dow.index, dow.High, "r--", label="Dow") 
plt. plot (kospi. index, kospi.High, "b", label="KOSPI")



# 해당 날짜 기준 증가 상승율, 상대 수익율

d= (dow.Close / dow.Close.loc["2010-06-01"]) * 100
k= (kospi.Close / dow.Close.loc["2010-06-01"])* 100 
plt.plot (d.index, "r--", label="Dow") 
plt.plot (k.index, "b", label="KOSPI")

plt.grid(True)

plt.legend()
plt.show() """



# 주식 데이터 분석

""" df = fdr.DataReader("KS11")
df0 = df.loc["2023"]


print(df0)

# df0["Open"].plot()
# df0["Close"].plot()
# df0["Low"].plot()
df0["Close"].plot()

plt.grid(True)



# 다우지수와 코스피 비교

dow = fdr.DataReader("DJI", "2010-06-01")
kospi = fdr.DataReader("KS11", "2010-06-01")




# 각 지수별 종가 기준 그래프 출력
plt.plot(dow.index, dow.Close, "r--", label="Dow")
plt.plot(kospi.index, kospi.Close, "b", label="KOSPI") """




# 국내 주식 코드 확인

""" import requests
from datetime import datetime
from matplotlib import dates as mdates
from bs4 import BeautifulSoup as bs


# 해당 데이터를 가져오는 URL
url = "https://finance.naver.com/item/sise_day.nhn?code=00530"
url = "https://finance.naver.com/item/sise_day.nhn?code=068270"




# 데이터 파싱

headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 
res = requests.get (url, headers=headers)
html = bs(res. text, "html. parser")
html_table = html. select ("table")
table = pd.read_html(str(html_table))
print (table)

df_list = []



# 해당 site 1~ 100 페이지 파싱

page = 1
for page in range(1, 100):
    page_url = f"{url}&page={page}"
    print(page_url)

    response = requests.get(page_url, headers=headers)
    html = bs(response.text, "html.parser")
    html_table = html.select("table")
    table = pd.read_html(str(html_table))

    if not table[0].empty:
        df_list.append(table[0].dropna())
        page += 1
    else:
        break

print (df_list)




# 데이터 처리

df = pd.concat(df_list, ignore_index=True)

df = df.dropna()
df = df.iloc[0:30]
df = df.sort_values(by="날짜")


plt.figure(figsize=(15, 5))
plt.title("Target (close)")
plt.xticks (rotation=45)
plt.plot(df["날짜"], df["종가"], "CO-")
plt.grid(color="gray", linestyle="--")
plt. show()  """



# 미국 개별 종목 분석

""" import yfinance as yf


# ticker 확인
#MS
ticker = "MSFT"



# Apple
# ticker = "APPL"
start_date = "2022-01-01"
end_date = "2023-12-02"

data = yf.download(ticker, start=start_date, end=end_date)

plt. figure(figsize=(12, 6))
plt.plot(data["Close"], label="Close Price")



# 평균 계산

# 50일 평균
data["MA_50"] = data["Close"].rolling(window=50).mean()

# 200일 평균
data["MA_200"] = data["Close"].rolling(window=200).mean()

plt.plot (data ["MA_50" ], lable = "50=day Mean Average")
plt. plot (data ["MA_200" ], lable = "200=day Mean Average")

plt.title("Stock Price")
plt.xlabel ("Data")
plt. ylabel ("Price ($)")
plt.legend ()
plt.show() """



# 국가별 인구 데이터 분석

""" import requests
from datetime import datetime
from matplotlib import dates as mdates
from bs4 import Beautiful as bs



# 데이터 다운로드 및 처리

url = "https://www.worldometers.info/world-population/population-by-country/"
response = requests. get (url)
soup = bs(response. text, "html. parser")

countries = []
populations = [] """



# 테이블 분석

rows = soup.select ("#example2 tbody tr")
for row in rows:
     columns = row.select ("td")
     country = columns[1].get_text(stjip=True)
     population = int(columns[2].get_text(strip=True).replace(","""))
     countries.append(country)
     populations.append(population)

top_countries = countries[: 10]
top_populations = populations[:10]

plt.figurw(figsize = (12, 6))
# plt.bar(top_countries[::-1], top_populations[::-1], color="skyblue")
plt.barh(top_countries[::-1], top_populations[::-1], color="skyblue")
plt.xlabel("Population")
plt.title("Top 10")
plt.show()