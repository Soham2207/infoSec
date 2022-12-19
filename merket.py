import hashlib

class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.hash = hashlib.sha256(str(data).encode("utf-8")).hexdigest()
        self.right = right

class MerkelTree:
    def __init__(self,leaves) :
        self.root = Node(leaves)
        open = [self.root]
        while len(open):
            node = open.pop(0)
            data = node.data
            half_data = len(data)//2
            if half_data:
                new_leaves = [Node(data[:half_data]),Node(data[half_data:])]
                node.left = new_leaves[0]
                node.right = new_leaves[1]
                open.extend(new_leaves)
    def printTree(self):
        node = self.root
        open = [node]
        while len(open):
            node = open.pop(0)
            print("Content: ",node.data)
            print("Hash: ",node.hash)
            node_right = node.right
            node_left = node.left
            if node_right is not None:
                open = [node_right] + open
            if node_left is not None:
                open = [node_left] + open
s = input("Enter the text : ")
tree = MerkelTree(s.split())
tree.printTree()