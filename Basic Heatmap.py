#!/usr/bin/python 
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font='SimHei')

df = pd.read_csv('Example Data.csv', engine='python')
flights = df.pivot(index='A',columns='B',values='VALUE')

f, ax = plt.subplots(figsize=(9,6)) #新建画布，更改画布长宽
pic = sns.heatmap(flights,cmap='YlOrRd',linewidths=0.5, square=True).invert_yaxis() #反转y轴标签顺序,改图片属性
ax.set(xlabel = 'B', ylabel= 'A') #加轴标题
ax.set_yticklabels(ax.get_yticklabels(), rotation=0) #旋转y轴标签文字

plt.show()
