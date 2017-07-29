#encoding=utf=8

class BinaryTreeNode(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    def setValue(self,value):
        self.value=value
    def getValue(self):
        return self.value
    def setLeftChild(self,Node):
        self.left=Node
    def setRightChild(self,Node):
        self.right=Node

class HuffmanTreeNode(BinaryTreeNode):
    def __init__(self,weight=0,value=None):
        BinaryTreeNode.__init__(self,value)
        self.weight=weight
    def setWeight(self,weight):
        '''
         内部结点拥有权值

        '''
        self.weight=weight
    def getWeight(self):
        return self.weight
    def setLeftChild(self,Node):
        BinaryTreeNode.setLeftChild(self,Node)
        self.weight+=Node.getWeight()
    def setRightChild(self,Node):
        BinaryTreeNode.setRightChild(self,Node)
        self.weight+=Node.getWeight()


if __name__ == '__main__':
    node1=HuffmanTreeNode(3,"B")
    node2=HuffmanTreeNode(14,"C")
    parent=HuffmanTreeNode()
    parent.setLeftChild(node1)
    parent.setRightChild(node2)
    print parent.weight