#encoding=utf-8
from linklist import *

'''
  实现一个链式队列
'''
class Queue(object):
    def __init__(self):
        self.front=None
        self.tail=None
        self.count=0
    def enqueue(self,data):
        "入队 实际是上就是链表的尾插法"
        if self.count==0:
            self.front=LinkList(data)
            self.tail=self.front
        else:
            temp=LinkList(data)
            self.tail.setNext(temp)
            self.tail=temp
        self.count+=1
    def dequeue(self):

        if self.count==0:
            return None
        else:
            temp=self.front.getData()
            self.front=self.front.getNext()
            self.count -=1
            return temp
    def __len__(self):
        return self.count
    def peek(self):
        '''
         return the front without removing it
        :return:
        '''
        if  self.count==0:
            return None
        else:
            return self.front.getData()
if __name__ == '__main__':
    queue=Queue()
    print queue
    print queue.front
    print queue.tail
    queue.enqueue("ee")
    print queue.front
    print queue.tail

    queue.enqueue(23)
    queue.enqueue("wang")
    print queue.tail
    print(len(queue))
    print queue.dequeue()
    print(len(queue))
    print queue.tail
    print queue.dequeue()
    print queue.dequeue()
    print queue.dequeue()
    print(len(queue))
