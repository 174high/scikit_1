#!/usr/bin/env python 
#coding=utf-8 

import sys

import matplotlib.pyplot as plt

import scipy as sp

data=sp.genfromtxt("C:\Users\Administrator\Desktop\machine_learning\web_traffic.tsv",delimiter="\t")


print(data[:10])

x=data[:,0]

y=data[:,1]

sp.sum(sp.isnan(y))

x=x[~sp.isnan(y)]

y=y[~sp.isnan(y)]


#设置有第一行的数据设置为 X轴 第二行的数据设置为 Y轴

plt.scatter(x,y)

#表的标题

plt.title("Web traffic over the last month")

#X轴的单位名字
plt.xlabel("Time")

#Y轴的单位名字
plt.ylabel("Hits/hour")

#设置X轴的自定义刻度  每隔  w*7*24 的时间安置一个 week *的自定义刻度 以便知道大概时间
plt.xticks([w*7*24 for w in range(10)],

['week %i'%w for w in range(10)])

#把下行注销掉试试，主要目的是如果后面没有数据，就自动截断到有数据的地方
plt.autoscale(tight=True)

#还不知道干什么
plt.grid()
 
#................machine leanring part...................
#fp1,residuals,rank,sv,rcond=sp.polyfit(x,y,1,full=True)
#
#f1=sp.poly1d(fp1)
#
#fx=sp.linspace(0,x[-1],1000)
#
#
#plt.plot(fx,f1(fx),linewidth=4)
#	   
#
#plt.legend(["d=%i" %f1.order],loc="upper left")
#........................................................

plt.show()






