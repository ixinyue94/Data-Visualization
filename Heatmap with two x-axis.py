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
ax1.set(xlabel = 'B', ylabel= 'A') 

ax2 = ax1.twiny() #新建ax1的镜像画布ax2
sns.heatmap(flights,ax=ax2, cmap='YlOrRd',linewidths=0.5,xticklabels=c, cbar=False).invert_yaxis() #设置ax2的横坐标标签为c，不显示色轴
ax2.xaxis.set_ticks_position('top') #设置ax2的横坐标位置为顶部
ax2.set(xlabel = 'C') #设置ax2的横轴名字

plt.show()
