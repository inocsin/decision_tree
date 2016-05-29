### dicision tree using ID3 algorithm
import readfile
import readtest
import gen_tree
import crossval
(x,y)=readfile.readtxt()
cro=crossval.croval(x,y)
mytree=gen_tree.tree(x,y)
# mytree.markTreeId()
# mytree.printTree()
mypre=mytree.precison(x,y)


# print type(x)
# print x
# print y
# print len(x)
# print mypre
print "The original precision is %.2f%%"%(mypre*100)
print "The precision of decision tree calculate by cross validation is %.2f%%"%(cro*100)
