from lib import TreeNode, BinaryTree
    
class Code:
    def serialize(self, root):
        if not root:
            return "#,"
        return str(root.val) + "," + self.serialize(root.left) + self.serialize(root.right)
    
    def deserialzie(self, data):
        data = data.split(",")
        startIndex = 0
        def toRootNode():
            nonlocal startIndex
            string = data[startIndex]
            if string == "#":
                startIndex += 1
                return None
            root = TreeNode(int(string))
            startIndex += 1
            root.left = toRootNode()
            root.right = toRootNode()
            return root
        return toRootNode()

c = Code()
tree = BinaryTree("5,4,8,11,null,13,4,7,2,null,null,null,1")
print(tree)
serialized_string = c.serialize(tree.get_root())
print("serialized string: " + serialized_string)
root = c.deserialzie(serialized_string)
print(BinaryTree(root))
