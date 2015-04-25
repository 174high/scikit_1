搭建机器学习平台和例子

http://www.gumpcs.com/index.php/archives/226/comment-page-1#comment-25

1.python_machine_learning                  是安装平台的软件
2.web_traffic.tsv                          软件需要的数据集
3.user_guide-0.11                          软件的用户使用手册
4.搭建python机器学习环境以及第一个例子.doc   
.........................................



.........................................

//导入数据

import scipy as sp

data=sp.genfromtxt("C:\Users\Administrator\Desktop\machinelearning\web_traffic.tsv",delimiter="\t")

print(data[:10])

print(data.shape)

sp.sum(sp.isnan(y))

x=x[~sp.innan(y)]


.........................................

//数据可视化

import matplotlib.pyplot as plt

plt.scatter(x,y)

plt.title("web traffic over the last month")

plt.xlabel("time")

plt.ylabel("hits/hour")

plt.xticks([w*7*24 for w in range(10)],)

plt.autoscale(tight=True)

plt.grid()

plt.show()

...............................................

//机器学习部分

def error(f,x,y):
return sp.sum((f(x)-y)**2)

fp1,residuals,rank,sv,rcond=sp.polyfit(x,y,1,full=True)

printf("Modle parametaer: %s"% fp1);

print(residuals)

..................................................

//整个脚本 machine.py 在本目录下

使用  python  machine.py 命令运行本脚本











