�����ѧϰƽ̨������

http://www.gumpcs.com/index.php/archives/226/comment-page-1#comment-25

1.python_machine_learning                  �ǰ�װƽ̨�����
2.web_traffic.tsv                          �����Ҫ�����ݼ�
3.user_guide-0.11                          ������û�ʹ���ֲ�
4.�python����ѧϰ�����Լ���һ������.doc   
.........................................



.........................................

//��������

import scipy as sp

data=sp.genfromtxt("C:\Users\Administrator\Desktop\machinelearning\web_traffic.tsv",delimiter="\t")

print(data[:10])

print(data.shape)

sp.sum(sp.isnan(y))

x=x[~sp.innan(y)]


.........................................

//���ݿ��ӻ�

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

//����ѧϰ����

def error(f,x,y):
return sp.sum((f(x)-y)**2)

fp1,residuals,rank,sv,rcond=sp.polyfit(x,y,1,full=True)

printf("Modle parametaer: %s"% fp1);

print(residuals)

..................................................

//�����ű� machine.py �ڱ�Ŀ¼��

ʹ��  python  machine.py �������б��ű�











