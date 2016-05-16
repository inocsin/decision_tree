# this file will calculate entropy and gain
from __future__ import division
import math

def ent(y):
    # y is n*1 column vector, different value of y indicate different class
    max_num=max(y)+1
    # print max_num
    mat=[0]*max_num
    # print mat
    ratio=[0]*max_num
    # print ratio
    for i in range(len(y)):
        mat[y[i]]+=1

    for i in range(max_num):
        ratio[i]=mat[i]/len(y)
    # print mat
    # print ratio
    # print type(ratio[0])
    entropy=0
    for i in range(len(ratio)):
        if ratio[i]!=0:
            entropy+=ratio[i]*math.log(ratio[i])/math.log(2)
    return -entropy
# y=[0,0,0,0,1,1,1,1]
# print ent(y)
def gain(x,y):
    # x and y is n*1 column vector, x is a attribute, y is the result of classification
    max_num=max(x)+1 # the x has max_num different value
    xx=[] # each element is a vector of y which correspond to different x value, xx is like [[],[],[]]
    for i in range(max_num):
        xx.append([])
    for i in range(len(x)):
        xx[x[i]].append(y[i])
    # print xx
    sigma=0
    for i in range(len(xx)):
        if len(xx[i])!=0:
            sigma=sigma+len(xx[i])/len(x)*ent(xx[i])
    # print "ent=",ent(y)
    # print "sigma=",sigma
    return ent(y)-sigma
# x=[0,1,1,1,0,1,0,0,1,0,1,0,1,1,1,1]
# y=[0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0]
# print gain(x,y)

