### build up decision tree
import cal_gain
import numpy as np
class node(object):
    def __init__(self,isleaf,classType,feaId,feaAmo):
        self.parent=None
        self.id=None
        self.leaf=None
        self.classType=None
        self.feaId=None
        self.feaAmo=None
        self.childNode=None
        if isleaf==True:
            self.leaf=isleaf
            self.classType=classType
        else:
            self.feaId=feaId #current feature type
            self.feaAmo=feaAmo #total possible value of this feature
            self.childNode=[] #child node correspond to different feature value
            for i in range(feaAmo):
                self.childNode.append(None)

    def addChild(self,otherNode,value):
        self.childNode[value]=otherNode

    def getid(self):
        return self.id
    def getNodeInf(self):
        return (self.leaf,self.classType,self.feaId,self.feaAmo)

    def getCertainChild(self,childid):
        return self.childNode[childid]

    def printNode(self):
        print "parent",self.parent
        print "id",self.id
        print "leaf=",self.leaf
        print "classType=",self.classType
        print "feaID=",self.feaId
        print "feaAmount",self.feaAmo
        print "----------------------------"

    def returnChild(self):
        return self.childNode

    def markNodeId(self,parent,thisnode):
        self.parent=parent
        self.id=thisnode



class tree(object):
    def __init__(self,x,y):
        self.root=None
        self.x=np.array(x)
        self.y=np.array(y)
        self.totalClass=max(y)+1
        self.totalAttr=len(x[0]) # record the total number of different attribute, x is a numpy.array type
        self.feaValue=[] # record each attribute have feaValue[i] different value
        for i in range(self.totalAttr):
            self.feaValue.append(max(self.x[:,i])+1)
        self.root=self.buildTree(self.x,self.y,[],None)

    def bestAttr(self,vecx,vecy,usedAttr):
        bestattr=-1
        bestgain=-1 # gain always >= 0
        for i in range(self.totalAttr):
            if not i in usedAttr: # attribue i is not used
                if cal_gain.gain(vecx[:,i],vecy)>bestgain:
                    bestattr=i
                    bestgain=cal_gain.gain(vecx[:,i],vecy)
        return (bestattr,bestgain,cal_gain.ent(vecy)) # tuple

    def calMostFreC(self,vecy): #calculate the most frequent class in set D, in case subset of D - Dv is empty
        mostFreC=-1
        count=0
        for i in range(self.totalClass):
            tmpcount=sum(np.array(vecy)==i)
            if tmpcount>count:
                mostFreC=i
                count=tmpcount
        return mostFreC


    def buildTree(self,vecx,vecy,usedAttr=[],frec=None):
        if len(vecy)==0:
            return node(True,frec,None,None)
        elif sorted(usedAttr)==range(self.totalAttr):
            frec=self.calMostFreC(vecy)
            return node(True,frec,None,None)
        else:
            frec=self.calMostFreC(vecy)
            (bestattr,bestgain,entr)=self.bestAttr(vecx,vecy,usedAttr)
            mynode=node(False,None,bestattr,self.feaValue[bestattr])
            usedAttrCur=usedAttr[:] # copy
            usedAttrCur.append(bestattr)
            for i in range(self.feaValue[bestattr]):
                index=(vecx[:,bestattr]==i)
                vecx_sub=vecx[index,:]
                vecy_sub=vecy[index]
                tmpnode=self.buildTree(vecx_sub,vecy_sub,usedAttrCur,frec)
                mynode.addChild(tmpnode,i)
            return mynode

    def markTreeId(self):
        queue=[]
        self.root.markNodeId(-1,0)
        queue.append(self.root)
        idcount=1
        while queue!=[]:
            tmpnode=queue[0]
            del queue[0]
            pid=tmpnode.getid()
            tmpchild=tmpnode.returnChild()
            if tmpchild!=None:
                for childnode in tmpchild:
                    childnode.markNodeId(pid,idcount)
                    idcount+=1
                    queue.append(childnode)


    def printTree(self):
        queue=[]
        queue.append(self.root)
        while queue!=[]:
            tmpnode=queue[0]
            tmpnode.printNode()
            del queue[0]
            if tmpnode.returnChild()!=None:
                queue.extend(tmpnode.returnChild())
        return True

    def predictClass(self,attrlist):
        curnode=self.root
        while True:
            (leaf,classType,feaId,feaAmo)=curnode.getNodeInf()
            if leaf==True:
                break
            curnode=curnode.getCertainChild(attrlist[feaId])
        return classType

    def precison(self,x,y):
        row=len(x) # here x is a m*n matrix, where m inicate the number of instance, n is the number of attribute
        rightPre=0
        for i in range(row):
            if self.predictClass(x[i])==y[i]:
                rightPre+=1
        pre=float(rightPre)/row
        return pre


















