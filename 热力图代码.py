#!/usr/bin/python 
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font='SimHei')
plt.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_csv('热力图数据示例.csv', engine='python')
flights = df.pivot(index="A",columns="B",values="VALUE")
f, ax = plt.subplots(figsize=(9,6)) #更改输出图片长宽
pic = sns.heatmap(flights,cmap='YlOrRd',linewidths=0.5, square=True).invert_yaxis() #反转y轴,改图片属性
ax.set(xlabel = 'B ', ylabel= 'A ') #加轴标题
ax.set_yticklabels(ax.get_yticklabels(), rotation=0)

plt.show(pic)