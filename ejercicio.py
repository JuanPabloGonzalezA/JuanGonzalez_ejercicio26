import matplotlib.pyplot as plt
import numpy as np

pimed=np.pi/2.0
g=9.8

pv=np.random.uniform(35,45,100000000)
pt=np.random.uniform(0,pimed,100000000)
pd=pv**2*np.sin(2*pt)/g
plt.hist(pv,normed=1,bins=100,alpha=0.8)

d1max=61.0+5.0
d1min=61.0-5.0
pv1=pv[np.logical_and(pd>d1min,pd<d1max)]
pt1=np.random.uniform(0,pimed,len(pv1))
pd1=pv1**2*np.sin(2*pt1)/g
plt.hist(pv1,normed=1,bins=100,alpha=0.8,label='1')

d2max=115.0+5.0
d2min=115.0-5.0
pv2=pv1[np.logical_and(pd1>d2min,pd1<d2max)]
pt2=np.random.uniform(0,pimed,len(pv2))
pd2=pv2**2*np.sin(2*pt2)/g
plt.hist(pv2,normed=1,bins=100,alpha=0.8,label='2')

d3max=31.0+5.0
d3min=31.0-5.0
pv3=pv2[np.logical_and(pd2>d3min,pd2<d3max)]
pt3=np.random.uniform(0,pimed,len(pv3))
pd3=pv3**2*np.sin(2*pt3)/g
plt.hist(pv3,normed=1,bins=100,alpha=0.8,label='3')

d4max=177.0+5.0
d4min=177.0-5.0
pv4=pv3[np.logical_and(pd3>d4min,pd3<d4max)]
pt4=np.random.uniform(0,pimed,len(pv4))
pd4=pv4**2*np.sin(2*pt4)/g
plt.hist(pv4,normed=1,bins=100,alpha=0.8,label='4')


plt.xlabel('v')
plt.ylabel('p')
plt.title('histograma velocidades')
plt.legend()

plt.savefig('histograma.png')
