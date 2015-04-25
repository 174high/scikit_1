#!/usr/bin/env python
import sys

import scipy as sp

data=sp.genfromtxt("C:\Users\Administrator\Desktop\machine_learning\web_traffic.tsv",delimiter="\t")


print(data[:10])

x=data[:,0]

y=data[:,1]

sp.sum(sp.isnan(y))

x=x[~sp.isnan(y)]

y=y[~sp.isnan(y)]

import matplotlib.pyplot as plt

plt.scatter(x,y)

plt.title("Web traffic over the last month")

plt.xlabel("Time")

plt.ylabel("Hits/hour")

plt.xticks([w*7*24 for w in range(10)],

['week %i'%w for w in range(10)])

plt.autoscale(tight=True)

plt.grid()

fp1,residuals,rank,sv,rcond=sp.polyfit(x,y,1,full=True)

f1=sp.poly1d(fp1)

fx=sp.linspace(0,x[-1],1000)

plt.plot(fx,f1(fx),linewidth=4)

plt.legend(["d=%i" %f1.order],loc="upper left")

plt.show()

input()
