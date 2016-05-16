# read file from test.txt, just for test use
import numpy as np
def readtxt():
    fp=open('test.txt','r')
    allLines=fp.readlines()
    fp.close()
    data=[line.strip() for line in allLines]
    raw_x=[line.split('\t') for line in data] #raw_x is a 27*6 matrix, each row is a instance
    raw_x=raw_x[1:] #the first row is not data
    # print raw_x
    x=[]
    y=[]
    for row in raw_x:
        if row[1]=='<35':
            age=0
        else:
            age=1
        if row[2]=='female':
            gender=0
        else:
            gender=1
        if row[3]=='l':
            income=0
        elif row[3]=='m':
            income=1
        else:
            income=2
        if row[4]=='n':
            cla=0
        else:
            cla=1
        x.append([age,gender,income])
        y.append(cla)
        xx=np.array(x)
    # for line in x:
    #     print line
    # print y
    # print len(x)
    # print len(y)
    return (x,y)
# (x,y)=readtxt()
# print x
# print y
