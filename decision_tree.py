

fp=open('file.txt','r')
allLines=fp.readlines()
fp.close()
data=[line.strip() for line in allLines]
raw_x=[line.split('\t') for line in data] #raw_x is a 27*6 matrix, each row is a instance
raw_x=raw_x[1:-1] #the first row is not data
x=[]
for row in raw_x:
    if row[1]=='<=30'
        age=0
    elif row[1]=='31-51'
        age=1
    else
        age=2
    if row[2]=='L'


