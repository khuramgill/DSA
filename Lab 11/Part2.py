# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 09:03:24 2023

@author: lenovo
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AvlTree:
    def __init__(self):
        self.root = None

    def Height(self, node):
        if not node:
            return 0
        return node.height

    def Balance_factor(self, node):
        if not node:
            return 0
        return self.Height(node.left) - self.Height(node.right)

    def Rotate_R(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = max(self.Height(y.left), self.Height(y.right)) + 1
        x.height = max(self.Height(x.left), self.Height(x.right)) + 1

        return x

    def Rotate_L(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = max(self.Height(x.left), self.Height(x.right)) + 1
        y.height = max(self.Height(y.left), self.Height(y.right)) + 1

        return y

    def Balance(self, node):
        if not node:
            return None

        node.height = max(self.Height(node.left), self.Height(node.right)) + 1

        balance = self.Balance_factor(node)

        if balance > 1:
            if self.Balance_factor(node.left) >= 0:
                return self.Rotate_R(node)
            else:
                node.left = self.Rotate_L(node.left)
                return self.Rotate_R(node)

        if balance < -1:
            if self.Balance_factor(node.right) <= 0:
                return self.Rotate_L(node)
            else:
                node.right = self.Rotate_R(node.right)
                return self.Rotate_L(node)

        return node

    def _insert(self, node, key):
        if not node:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node

        return self.Balance(node)

    def FindMiniVal_N(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def Remove(self, node, key):
        if not node:
            return None

        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if not node.left or not node.right:
                temp = node.left if node.left else node.right

                if not temp:
                    temp = node
                    node = None
               

                del temp
            else:
                temp = self.FindMiniVal_N(node.right)
                node.key = temp.key
                node.right = self.Remove(node.right, temp.key)

        if not node:
            return None

        return self.Balance(node)

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def remove(self, key):
        self.root = self.Remove(self.root, key)
    
    def visualize_tree(self, node, level=0, prefix="Root: "):
        if node:
            print("    " * level + prefix + str(node.key))
            if node.left or node.right:
                if node.left:
                    self.visualize_tree(node.left, level + 1, "L ")
                if node.right:
                    self.visualize_tree(node.right, level + 1, "R  ")


   
# Example usage
avl = AvlTree()
keys = [30, 20, 40, 10, 25, 35, 50]

for key in keys:
    avl.insert(key)

avl.visualize_tree(avl.root)
