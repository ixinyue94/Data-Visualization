#!/usr/bin/python 
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font='SimHei')

df = pd.read_csv('热力图数据示例.csv', engine='python')
flights = df.pivot(index='A',columns='B',values='VALUE')

c = []
for i in range(len(df)):
    if df.loc[i,'C'] not in c:
        c.append(df.loc[i,'C'])

f, ax1 = plt.subplots(figsize=(9,6))
sns.heatmap(flights,ax=ax1, cmap='YlOrRd',linewidths=0.5).invert_yaxis()
ax1.set(xlabel = 'B', ylabel= 'A') #加轴标题

ax2 = ax1.twiny()
sns.heatmap(flights,ax=ax2, cmap='YlOrRd',linewidths=0.5,xticklabels=c, cbar=False).invert_yaxis()
ax2.xaxis.set_ticks_position('top')
ax2.set(xlabel = 'C')

plt.show()
