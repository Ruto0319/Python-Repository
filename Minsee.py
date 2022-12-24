
from math import *
from matplotlib import pyplot as plt


xx = open("TTT.txt", 'w')

for i in range(100):
    data = 4*sin(i*pi*0.08)
    data2 = 2*sin(i*pi*0.05)
    xx.write("{}\n".format(data))
xx.close()

yy = open("TTT.txt",'r')

B = yy.readline()
Btxt = []

while B != "":
    B == yy.readline()
    B = B.strip('\n')
    Btxt.append(B)

Ctxt = []
for i in range(99):
    C = Btxt[i]
    C = float(C)
    Ctxt.append(C)

x = []
for i in range(99):
    x.append(i)

print(x)

