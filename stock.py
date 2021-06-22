import requests
stock=input("請輸入股票代碼")
res = requests.get('https://tw.stock.yahoo.com/_td-stock/api/resource/FinanceChartService.ApacLibraCharts;symbols=%5B%22'+stock+'.TW%22%5D;type=tick?bkt=%5B%22tw-qsp-exp-no2-1%22%2C%22test-es-module-production%22%2C%22test-portfolio-stream%22%5D&device=desktop&ecma=modern&feature=ecmaModern%2CshowPortfolioStream&intl=tw&lang=zh-Hant-TW&partner=none&prid=2h3pnulg7tklc&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.902&returnMeta=true')
res

jd = res.json()['data']

close = jd[0]['chart']['indicators']['quote'][0]['close']

timestamp = jd[0]['chart']['timestamp']

import pandas
df = pandas.DataFrame({'timestamp': timestamp, 'close':close})

df.head()
df['dt'] = pandas.to_datetime(df['timestamp'] + 3600 * 8, unit = 's')

get_ipython().run_line_magic('matplotlib', 'inline')
df.plot('dt', 'close', figsize = [20,10])





