class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _balance(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node):
        if node:
            node.height = 1 + max(self._height(node.left), self._height(node.right))

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        self._update_height(node)

        balance = self._balance(node)

        # Left-Left Case
        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)

        # Right-Right Case
        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)

        # Left-Right Case
        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right-Left Case
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self._update_height(z)
        self._update_height(y)

        return y

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self._update_height(y)
        self._update_height(x)

        return x

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._get_min(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        self._update_height(node)

        balance = self._balance(node)

        # Left-Left Case
        if balance > 1 and self._balance(node.left) >= 0:
            return self._rotate_right(node)

        # Right-Right Case
        if balance < -1 and self._balance(node.right) <= 0:
            return self._rotate_left(node)

        # Left-Right Case
        if balance > 1 and self._balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right-Left Case
        if balance < -1 and self._balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _get_min(self, node):
        while node.left is not None:
            node = node.left
        return node
