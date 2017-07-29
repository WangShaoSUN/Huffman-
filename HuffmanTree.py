#encoding=utf-8
import heapq
from HuffmanNode import *
class HuffmanTree(object):
    def __init__(self,root=None):
          pass


# def encode():
#      pass
def createNodes():
      docStr="DDaaaabbbbbccccccc"
      nodeDic={}
      for i in docStr:
          try:
            temp= nodeDic[i]
            temp.setWeight(temp.getWeight()+1)
          except KeyError:
            nodeDic[i]=HuffmanTreeNode(1,i)
      allNodes=nodeDic.values()
      # help(sorted)
      def com(x,y):
          if x.weight-y.weight:
              return 1
          else:
              return 0
      all1=sorted(allNodes,key=lambda x:x.weight,reverse=False)
      # print all1[3].weight
      # help(list)
      while len(all1)>1:
          temp=HuffmanTreeNode()
          temp1=all1.pop(0)
          temp2=all1.pop(0)
          temp.setLeftChild(temp1)
          temp.setRightChild(temp2)
          all1.append(temp)
          all1=sorted(all1,key=lambda x:x.weight,reverse=False)
      # print len(all1)
      print all1[0].weight
      #     print all1.pop(0).value


      # print b.value,b.weight
createNodes()
