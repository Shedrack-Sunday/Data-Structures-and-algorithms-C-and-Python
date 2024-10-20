class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinaryTree:
    def __init__(self):
        self.root = None

    # Insert a new node in the tree
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    # Recursive function to insert a new node
    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    # Inorder traversal of the tree
    def inorder_traversal(self):
        return self._inorder_recursive(self.root)

    # Recursive inorder traversal
    def _inorder_recursive(self, current_node):
        elements = []
        if current_node:
            elements += self._inorder_recursive(current_node.left)
            elements.append(current_node.value)
            elements += self._inorder_recursive(current_node.right)
        return elements

    # Preorder traversal of the tree
    def preorder_traversal(self):
        return self._preorder_recursive(self.root)

    # Recursive preorder traversal
    def _preorder_recursive(self, current_node):
        elements = []
        if current_node:
            elements.append(current_node.value)
            elements += self._preorder_recursive(current_node.left)
            elements += self._preorder_recursive(current_node.right)
        return elements

    # Postorder traversal of the tree
    def postorder_traversal(self):
        return self._postorder_recursive(self.root)

    # Recursive postorder traversal
    def _postorder_recursive(self, current_node):
        elements = []
        if current_node:
            elements += self._postorder_recursive(current_node.left)
            elements += self._postorder_recursive(current_node.right)
            elements.append(current_node.value)
        return elements



