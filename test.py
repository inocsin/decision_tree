class tree(object):
    def __init__(self,idd):
        self.idd=idd
    def changeid(self,idd):
        self.idd=idd
    def showid(self):
        print self.idd

def func(node):
    node=tree(2)
    node.changeid(10)

mynode=tree(1)
mynode.showid()
func(mynode)
mynode.showid()
