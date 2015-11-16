#!~/Pythonenv/bin/python
# -*- coding: utf-8 -*-


#author:mingzailao
#date:2015-11-12
#Based on numpy and matplotlib almost
#  citing the matplotlib :
# @Article{Hunter:2007,
#   Author    = {Hunter, J. D.},
#   Title     = {Matplotlib: A 2D graphics environment},
#   Journal   = {Computing In Science \& Engineering},
#   Volume    = {9},
#   Number    = {3},
#   Pages     = {90--95},
#   abstract  = {Matplotlib is a 2D graphics package used for Python
#   for application development, interactive scripting, and
#   publication-quality image generation across user
#   interfaces and operating systems.},
#   publisher = {IEEE COMPUTER SOC},
#   year      = 2007
# }


#this program is based on 3-D ,the demention of the vector must be 3,the 2 demention program is under working.

from numpy import *
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
import matplotlib.pyplot as plt
import operator


def c(n,k):
    if k!=0:
        return  reduce(operator.mul, range(n - k + 1, n + 1)) /reduce(operator.mul, range(1, k +1))
    else:
        return 1

def getPoint():
    dim=input("please enter the dimention you want:\n")
    n=4
    Points=np.zeros([n,dim])
    for i in range(n):
        Points[i]=np.asarray(input("please enter the point\n"),float)
    return Points

def Bernstein(n,k,t):
    return c(n,k)*(t**k)*((1-t)**(n-k))
def Bezier(Points,T):
    B=np.zeros([T.size,Points.shape[1]])
    for j in range(T.size):
        for i in range(Points.shape[0]):
            B[j]=B[j]+Bernstein(Points.shape[0]-1,i,T[j])*Points[i]
    return B.transpose()
def TwoBezier(P,alpha):
    a=P[P.shape[0]-1]+alpha*(P[P.shape[0]-1]-P[P.shape[0]-2])
    Q=np.asarray([P[P.shape[0]-1],a,np.asarray(input("Please enter 3th Point\n")),np.asarray(input("Please Enter 4th Point\n"))])
    return Q
P=getPoint();
PP=P.transpose()
alpha=2


P1=TwoBezier(P,alpha)
PP1=P1.transpose()

P2=TwoBezier(P1,alpha)
PP2=P2.transpose()

u=r_[0:1:0.001]
x=Bezier(P,u)[0]
y=Bezier(P,u)[1]
z=Bezier(P,u)[2]
x1=Bezier(P1,u)[0]
y1=Bezier(P1,u)[1]
z1=Bezier(P1,u)[2]
x2=Bezier(P2,u)[0]
y2=Bezier(P2,u)[1]
z2=Bezier(P2,u)[2]

fig=plt.figure()
ax=p3.Axes3D(fig)
plt.plot(PP[0],PP[1],PP[2],'mo:')

ax.plot_wireframe(x,y,z,color='b')
ax.plot_wireframe(x1,y1,z1,color='r')
ax.plot_wireframe(x2,y2,z2,color='c')

plt.plot(PP1[0],PP1[1],PP1[2],'mo:')
plt.plot(PP2[0],PP2[1],PP2[2],'mo:')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

