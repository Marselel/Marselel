class Tree(object):
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

node = Tree(7)
node.left=Tree(5)
node.right=Tree(8)
node.left.left=Tree(4)
node.left.right=Tree(6)
node.right.right=Tree(9)
def rec(node):
    if node:
        print(node.val)
        rec(node.right)
        rec(node.left)
rec(node)