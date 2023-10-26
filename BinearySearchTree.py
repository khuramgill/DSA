class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def _insert(self, root, item):
        if root == None:
            return Node(item)
        if root.value > item:
            root.left = self._insert(root.left,item)
        else:
            root.right = self._insert(root.right,item)
        return root
        
    def insert(self, item):
        self.root = self._insert(self.root, item)
        
    # def delt(self,item):
    #     self.root = self._delt(self.root,item)
        
    # def _delt(self, root , item):
    #     if root == None:
    #         return root
    #     if root.value > item:
    #         root.left = self._delt(root.left,item)
    #     elif root.value < item:
    #         root.right = self._delt(root.right, item)
    #     # Checking the Node with one or no childs
    #     else:
            
    #         if root.left is None:
    #             return root.right
    #         elif root.right is None:
    #             return root.left
    #         # Node with two children: Get the inorder successor (smallest
    #         # in the right subtree) and replace the current node's key
    #         temp = self.get_min_value_node(root.right)
    #         root.value = temp

    #         # Delete the inorder successor
    #         root.right = self._delt(root.right, root.value)

    #     return root
    
    # def get_min_value_node(self,root):
    #     temp = root
    #     while temp is not None:
    #         temp = temp.left
    #     return temp
    
    def in_order_traversal(self):
        result = []
        self._in_order_traversal(self.root, result)
        return result

    def _in_order_traversal(self, root, result):
        if root:
            self._in_order_traversal(root.left, result)
            result.append(root.value)
            self._in_order_traversal(root.right, result)
    
    
bst = BinarySearchTree()
keys = [8, 3, 10, 1, 6, 14, 4, 7, 13]

for key in keys:
    bst.insert(key)

print("Before Del:", bst.in_order_traversal())
# print("After Del:", bst.in_order_traversal())


    

            
            
            
            
        
        
        
            
        
            