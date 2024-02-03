class Node:
    def __init__(self, key, color, parent=None, left=None, right=None):
        self.key = key
        self.color = color  # 'R' for red, 'B' for black
        self.parent = parent
        self.left = left
        self.right = right


class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = Node(None, 'B')
        self.root = self.NIL_LEAF

    def insert(self, key):
        new_node = Node(key, 'R')
        new_node.left = self.NIL_LEAF
        new_node.right = self.NIL_LEAF

        parent = None
        current = self.root
        while current != self.NIL_LEAF:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        if new_node.parent is None:
            new_node.color = 'B'
            return

        if new_node.parent.parent is None:
            return

        self._fix_insert(new_node)

    def _fix_insert(self, node):
        while node.color == 'R' and node.parent.color == 'R':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'R':
                    node.parent.color = 'B'
                    uncle.color = 'B'
                    node.parent.parent.color = 'R'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'R':
                    node.parent.color = 'B'
                    uncle.color = 'B'
                    node.parent.parent.color = 'R'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self._left_rotate(node.parent.parent)

            if node == self.root:
                break

        self.root.color = 'B'

    def delete(self, key):
        target = self._find_node(key)
        if target is not None:
            self._delete_node(target)

    def _find_node(self, key):
        current = self.root
        while current != self.NIL_LEAF:
            if key == current.key:
                return current
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    def _delete_node(self, node):
        y = node
        y_original_color = y.color
        if node.left == self.NIL_LEAF:
            x = node.right
            self._transplant(node, node.right)
        elif node.right == self.NIL_LEAF:
            x = node.left
            self._transplant(node, node.left)
        else:
            y = self._minimum(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self._transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color
        if y_original_color == 'B':
            self._fix_delete(x)

    def _minimum(self, node):
        while node.left != self.NIL_LEAF:
            node = node.left
        return node

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _fix_delete(self, node):
        while node != self.root and node.color == 'B':
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == 'R':
                    sibling.color = 'B'
                    node.parent.color = 'R'
                    self._left_rotate(node.parent)
                    sibling = node.parent.right
                if sibling.left.color == 'B' and sibling.right.color == 'B':
                    sibling.color = 'R'
                    node = node.parent
                else:
                    if sibling.right.color == 'B':
                        sibling.left.color = 'B'
                        sibling.color = 'R'
                        self._right_rotate(sibling)
                        sibling = node.parent.right
                    sibling.color = node.parent.color
                    node.parent.color = 'B'
                    sibling.right.color = 'B'
                    self._left_rotate(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == 'R':
                    sibling.color = 'B'
                    node.parent.color = 'R'
                    self._right_rotate(node.parent)
                    sibling = node.parent.left
                if sibling.right.color == 'B' and sibling.right.color == 'B':
                    sibling.color = 'R'
                    node = node.parent
                else:
                    if sibling.left.color == 'B':
                        sibling.right.color = 'B'
                        sibling.color = 'R'
                        self._left_rotate(sibling)
                        sibling = node.parent.left
                    sibling.color = node.parent.color
                    node.parent.color = 'B'
                    sibling.left.color = 'B'
                    self._right_rotate(node.parent)
                    node = self.root
        node.color = 'B'

    def _left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left != self.NIL_LEAF:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def _right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right != self.NIL_LEAF:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node != self.NIL_LEAF:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

if __name__ == "__main__":
    rb_tree = RedBlackTree()
    
    keys = [7, 3, 18, 10, 22, 8, 11, 26, 2, 6, 13]
    for key in keys:
        rb_tree.insert(key)
    
    print("Inorder Traversal of Red-Black Tree:")
    print(rb_tree.inorder_traversal())
    
    key_to_delete = 18
    rb_tree.delete(key_to_delete)
    print(f"Deleted node with key {key_to_delete}.")
    
    print("Inorder Traversal after deletion:")
    print(rb_tree.inorder_traversal())
