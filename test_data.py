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


#�����е�һ�е���������Ϊ X�� �ڶ��е���������Ϊ Y��

plt.scatter(x,y)

#��ı���

plt.title("Web traffic over the last month")

#X��ĵ�λ����
plt.xlabel("Time")

#Y��ĵ�λ����
plt.ylabel("Hits/hour")

#����X����Զ���̶�  ÿ��  w*7*24 ��ʱ�䰲��һ�� week *���Զ���̶� �Ա�֪�����ʱ��
plt.xticks([w*7*24 for w in range(10)],

['week %i'%w for w in range(10)])

#������ע�������ԣ���ҪĿ�����������û�����ݣ����Զ��ضϵ������ݵĵط�
plt.autoscale(tight=True)

#����֪����ʲô
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






