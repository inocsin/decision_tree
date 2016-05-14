
def readtxt():
    fp=open('file.txt','r')
    allLines=fp.readlines()
    fp.close()
    data=[line.strip() for line in allLines]
    raw_x=[line.split('\t') for line in data] #raw_x is a 27*6 matrix, each row is a instance
    raw_x=raw_x[1:] #the first row is not data
    x=[]
    y=[]
    for row in raw_x:
        if row[1]=='<=30':
            age=0
        elif row[1]=='31-51':
            age=1
        else:
            age=2
        if row[2]=='L':
            education=0
        elif row[2]=='M':
            education=1
        else:
            education=2
        if row[3]=='\xe2\x85\xa0':
            area=0
        else:
            area=1
        if row[4]=='low':
            level=0
        elif row[4]=='medium':
            level=1
        else:
            level=2
        if row[5]=='bad':
            cla=0
        else:
            cla=1
        x.append([age,education,area,level])
        y.append(cla)
    # for line in x:
    #     print line
    # print y
    # print len(x)
    # print len(y)
    return (x,y)