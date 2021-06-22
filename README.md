# CS381A

開放平台軟體Final Project: 台股個股的當日股價走勢

### 簡介
此程式利用Python網路爬蟲Yahoo股市資料，User查詢個股代碼就能觀看當日股價走勢
![image](https://github.com/happy34083408/CS381A/blob/main/twstock.jpg)
### 步驟
1.直接輸入個股代碼

![image](https://github.com/happy34083408/CS381A/blob/main/input.jpg)

2.顯示個股股價的走勢

### 程式實作
我使用了Jupyter Notebook當作開發環境

> 1.開啟cmd命令提示字元，安裝爬蟲所需的套件
![image](https://github.com/happy34083408/CS381A/blob/main/cmd.jpg)
```
pip install requests
pip install pandas
pip install lxml
```

> 2.使用**requests**套件，並且在奇摩股市的API透過**get**抓取資料，使用者輸入代碼指定給stock
```
import requests
stock=input("請輸入股票代碼")
res = requests.get('https://tw.stock.yahoo.com/_td-stock/api/resource/FinanceChartService.ApacLibraCharts;symbols=%5B%22'+stock+'.TW%22%5D;type=tick?bkt=%5B%22tw-qsp-exp-no2-1%22%2C%22test-es-module-production%22%2C%22test-portfolio-stream%22%5D&device=desktop&ecma=modern&feature=ecmaModern%2CshowPortfolioStream&intl=tw&lang=zh-Hant-TW&partner=none&prid=2h3pnulg7tklc&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.902&returnMeta=true')
res
```

> 3.將資料存取在**json**，**json**可以當作個字典
```
jd = res.json()['data']
```

> 4.分析資料後，取得收盤價**close**
```
close = jd[0]['chart']['indicators']['quote'][0]['close']
```

> 5.取得時間搓**timestamp**
```
timestamp = jd[0]['chart']['timestamp']
```

> 6.把取得的資料結果暫時呈現出來，這邊**timestamp**的時間是unix time
![image](https://github.com/happy34083408/CS381A/blob/main/df.jpg)
```
import pandas
df = pandas.DataFrame({'timestamp': timestamp, 'close':close})
df.head()
```

> 7.切換成台灣時間
```
df['dt'] = pandas.to_datetime(df['timestamp'] + 3600 * 8, unit = 's')
```

> 8.把走勢圖畫出來，並且把圖放大，(此圖為2330台積電20210622的股價走勢)
![image](https://github.com/happy34083408/CS381A/blob/main/result.jpg)
```
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot('dt', 'close', figsize = [20,10])
```

### 討論
Q1.數據是否正確?
A.正確，但是2330台積電的20210622股價走勢，拿奇摩股市與實作結果相比沒什麼比較性，所以我另外查詢了2610華航的20210622股價走勢，可以發現相似度極高

< 2610(實作結果)
![image](https://github.com/happy34083408/CS381A/blob/main/2610.jpg)

< 2610華航(奇摩股市)
![image](https://github.com/happy34083408/CS381A/blob/main/yahoo2610.jpg)

### 參考
- 套件:https://weikaiwei.com/finance/python-stock-crawler/
- python繪圖:https://medium.com/%E6%95%B8%E6%93%9A%E4%B8%8D%E6%AD%A2-not-only-data/%E6%B7%B1%E5%85%A5%E6%B7%BA%E5%87%BA-python-%E8%A6%96%E8%A6%BA%E5%8C%96%E5%A5%97%E4%BB%B6-matplotlib-seaborn-%E6%A0%B8%E5%BF%83%E6%8C%87%E5%8D%97%E8%88%87%E7%B9%AA%E8%A3%BD-44a47458912
- 股市資料:https://tw.stock.yahoo.com/
