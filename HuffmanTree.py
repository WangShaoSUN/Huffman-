#encoding=utf-8
from  HuffmanNode import *
import pickle
# help(HuffmanTreeNode)
class HuffmanCompress(object):
    def __init__(self,doc="dddcccccabbeeee"):
        self.doc=doc
        self.root=self.createHuffmanNodes()
        self.codeDic={}
        self.parseCodeDic(self.root,"")
        print self.codeDic
        pass
    def createHuffmanNodes(self):
        nodeDic={}
        for i in self.doc:
            try:
                temp=nodeDic[i]
                temp.setWeight(temp.getWeight()+1)
            except:
                nodeDic[i]=HuffmanTreeNode(1,i)
        # print nodeDic
        allNodes=nodeDic.values()
        allNodes=sorted(allNodes,key=lambda x:x.weight,reverse=False)
        # print allNodes[2].value
        while len(allNodes)>1:
            temp=HuffmanTreeNode()
            temp1=allNodes.pop(0)
            temp2=allNodes.pop(0)
            temp.setLeftChild(temp1)
            temp.setRightChild(temp2)
            allNodes.append(temp)
            allNodes=sorted(allNodes,key=lambda x:x.weight,reverse=False)
        # print allNodes[0].weight
        return allNodes[0]
    def parseCodeDic(self,currentNode,code=""):
        if currentNode==None:
            return
        else:
            if currentNode.getValue()!=None:
                self.codeDic[currentNode.value]=code
            self.parseCodeDic(currentNode.left,code+"0")
            self.parseCodeDic(currentNode.right,code+"1")
    def convertToBinary(self):
        binstr=""
        # self.doc="aa"
        for x in self.doc:
            binstr+=self.codeDic[x]
        return binstr
    def writeFile(self):
        output=open("data.bin","wb")
        # pickle.dump(self.codeDic,output,2)
        pickle.dump(self.convertToBinary(),output,2)
        output.close()


        output=open("data.bin","rb")

        orgstr=pickle.load(output)
        print orgstr
    def decodeFile(self,doc):
        input=open(doc,"rb")
        self.codeDic=pickle.load(input)
        orgstr=pickle.load(input)
        print orgstr
        reverseDic={}
        for x in self.codeDic:
            reverseDic[self.codeDic[x]]=x
        print reverseDic
        begIndex=curIndex=0
        rebuildstr=""
        while curIndex<len(orgstr)+1:
            try:
                rebuildstr+=reverseDic[str(orgstr[begIndex:curIndex])]
                begIndex=curIndex
            except:
                curIndex+=1
        # print rebuildstr
        output=open("rebuild.txt","w")
        output.write(rebuildstr)
file=open("myths.txt","r")
# huff=HuffmanCompress(file.read())
huff=HuffmanCompress()

# huff.createHuffmanNodes()
print len(huff.convertToBinary())
huff.writeFile()
# huff.decodeFile("data.bin")