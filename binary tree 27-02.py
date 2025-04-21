class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Creation of Various nodes of Binary Tree as objects of TreeNode class

root = TreeNode("R")
nodeA = TreeNode("A")
nodeB = TreeNode("B")
nodeC = TreeNode("C")
nodeD = TreeNode("D")
nodeE = TreeNode("E")
nodeF = TreeNode("F")
nodeG = TreeNode("G")

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

print(root.right.right.data)
print(root.left.right.data)
print(nodeF.data)


# def preorder(root):
#     if root:
#         print(root.val, end=" ")
#         preorder(root.left)
#         preorder(root.right)
#
# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.val, end=" ")
#         inorder(root.right)
#
# def postorder(root):
#     if root:
#         postorder(root.left)
#         postorder(root.right)
#         print(root.val, end=" ")
