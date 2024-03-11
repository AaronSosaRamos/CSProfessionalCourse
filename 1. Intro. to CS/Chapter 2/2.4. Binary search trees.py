class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert_recursively(self.root, key)

    def _insert_recursively(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursively(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursively(node.right, key)

    def search(self, key):
        return self._search_recursively(self.root, key)

    def _search_recursively(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursively(node.left, key)
        return self._search_recursively(node.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursively(self.root, result)
        return result

    def _inorder_traversal_recursively(self, node, result):
        if node:
            self._inorder_traversal_recursively(node.left, result)
            result.append(node.key)
            self._inorder_traversal_recursively(node.right, result)


# Example usage of Binary Search Tree
bst = BinarySearchTree()

# Insert some keys
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(17)

# Search for a key
print("Search 7:", bst.search(7).key)  # Output: TreeNode object

# Inorder traversal
print("Inorder Traversal:", bst.inorder_traversal())  # Output: [3, 5, 7, 10, 12, 15, 17]
