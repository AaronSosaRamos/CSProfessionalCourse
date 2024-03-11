# Define B+ tree node and B+ tree classes
class BPlusTreeNode:
    def __init__(self, leaf=False):
        self.keys = []
        self.children = []
        self.leaf = leaf
        self.next = None

class BPlusTree:
    def __init__(self, degree):
        self.root = BPlusTreeNode(leaf=True)
        self.degree = degree

    def insert(self, key):
        if key in self.root.keys:
            return False
        if len(self.root.keys) == (2 * self.degree) - 1:
            new_root = BPlusTreeNode()
            new_root.children.append(self.root)
            self.split(new_root, 0)
            self.root = new_root
        self._insert(self.root, key)
        return True

    def _insert(self, node, key):
        if node.leaf:
            index = 0
            for i, k in enumerate(node.keys):
                if key > k:
                    index = i + 1
            node.keys.insert(index, key)
        else:
            index = 0
            for i, k in enumerate(node.keys):
                if key > k:
                    index = i + 1
            if len(node.children[index].keys) == (2 * self.degree) - 1:
                self.split(node, index)
                if key > node.keys[index]:
                    index += 1
            self._insert(node.children[index], key)

    def split(self, parent, index):
        node = parent.children[index]
        new_node = BPlusTreeNode(leaf=node.leaf)
        parent.keys.insert(index, node.keys[self.degree - 1])
        parent.children.insert(index + 1, new_node)
        new_node.keys = node.keys[self.degree:]
        node.keys = node.keys[:self.degree]

        if not node.leaf:
            new_node.children = node.children[self.degree:]
            node.children = node.children[:self.degree]

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if key in node.keys:
            return True
        if node.leaf:
            return False
        index = 0
        for i, k in enumerate(node.keys):
            if key > k:
                index = i + 1
        return self._search(node.children[index], key)

    def traverse(self):
        if self.root:
            self._traverse(self.root)

    def _traverse(self, node):
        if node:
            print(node.keys)
            if not node.leaf:
                for child in node.children:
                    self._traverse(child)


# Example usage of B+ tree
bplus_tree = BPlusTree(degree=2)

# Insert some keys
bplus_tree.insert(10)
bplus_tree.insert(20)
bplus_tree.insert(5)
bplus_tree.insert(15)
bplus_tree.insert(25)

# Search for keys
print(bplus_tree.search(10))  # Output: True
print(bplus_tree.search(15))  # Output: True
print(bplus_tree.search(30))  # Output: False

# Traverse the B+ tree
bplus_tree.traverse()