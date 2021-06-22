#!/usr/bin/env python
# coding: utf-8

# In[9]:


import requests
stock=input("請輸入股票代碼")
res = requests.get('https://tw.stock.yahoo.com/_td-stock/api/resource/FinanceChartService.ApacLibraCharts;symbols=%5B%22'+stock+'.TW%22%5D;type=tick?bkt=%5B%22tw-qsp-exp-no2-1%22%2C%22test-es-module-production%22%2C%22test-portfolio-stream%22%5D&device=desktop&ecma=modern&feature=ecmaModern%2CshowPortfolioStream&intl=tw&lang=zh-Hant-TW&partner=none&prid=2h3pnulg7tklc&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.902&returnMeta=true')
res


# In[10]:


jd = res.json()['data']


# In[11]:


close = jd[0]['chart']['indicators']['quote'][0]['close']


# In[12]:



timestamp = jd[0]['chart']['timestamp']


# In[13]:


import pandas
df = pandas.DataFrame({'timestamp': timestamp, 'close':close})


# In[14]:


df.head()


# In[15]:


df['dt'] = pandas.to_datetime(df['timestamp'] + 3600 * 8, unit = 's')


# In[16]:


get_ipython().run_line_magic('matplotlib', 'inline')
df.plot('dt', 'close', figsize = [20,10])


# In[ ]:




