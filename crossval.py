# cross validation, here we use Leave-One-Out
import copy
import gen_tree
def croval(x,y):
    sample=len(x) #record the total sample number
    mypre=0
    for i in range(sample):
        tmpx=copy.deepcopy(x)
        tmpy=copy.deepcopy(y)
        del tmpx[i]
        del tmpy[i]
        # print x
        # print '---------------------------------'
        # print tmpx
        # print '================================='

        mytree=gen_tree.tree(tmpx,tmpy)
        # mytree.markTreeId()
        # mytree.printTree()
        if mytree.predictClass(x[i])==y[i]:
            mypre+=1
            print i
    mypre=float(mypre)/float(sample)
    return mypre
