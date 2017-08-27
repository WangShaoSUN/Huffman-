#encoding=utf-8
'''
  a simple class for linklist study
'''
class LinkList(object):
    def __init__(self,data):
        self.data=data
        self.next=None
    def setData(self,data):
        self.data=data
    def getData(self):
        return self.data
    def setNext(self,next):
        self.next=next
    def getNext(self):
        return self.next
    def __str__(self):
        "return the data as string format"
        return  self.data
if __name__ == '__main__':
     current=LinkList("head")
     head=current
     for i in xrange(10):
         temp=LinkList(i)
         current.setNext(temp)
         current=current.getNext()
     while head!=None:
         print str(head.data)
         head=head.getNext()