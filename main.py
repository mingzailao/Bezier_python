
#!-utf8-
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
#the number of the control point can be  larger than 4 which means it can plot more than 3 times  Bezier curve.
#the other curve ,I set the last Control Point to be the first Control Point of the first Bezier curve.

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
    n=input("please enter the number of the point\n")
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
    return B.transpose();



P=getPoint();
alpha=2
a=P[P.shape[0]-1]+alpha*(P[P.shape[0]-1]-P[P.shape[0]-2])
P_next=np.asarray([P[P.shape[0]-1],a,P[0]])

u=r_[0:1:0.001]
x=Bezier(P,u)[0]
y=Bezier(P,u)[1]
z=Bezier(P,u)[2]
x_next=Bezier(P_next,u)[0]
y_next=Bezier(P_next,u)[1]
z_next=Bezier(P_next,u)[2]
fig=plt.figure()
ax=p3.Axes3D(fig)
ax.plot_wireframe(x,y,z)
ax.plot_wireframe(x_next,y_next,z_next,color='r')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

