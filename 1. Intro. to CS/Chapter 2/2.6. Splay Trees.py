class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class SplayTree:
    def __init__(self):
        self.root = None

    def _splay(self, x):
        while x.parent:
            if not x.parent.parent:
                if x == x.parent.left:
                    self._rotate_right(x.parent)
                else:
                    self._rotate_left(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                self._rotate_right(x.parent.parent)
                self._rotate_right(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                self._rotate_left(x.parent.parent)
                self._rotate_left(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                self._rotate_left(x.parent)
                self._rotate_right(x.parent)
            else:
                self._rotate_right(x.parent)
                self._rotate_left(x.parent)

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
            return

        current = self.root
        while current:
            if key < current.key:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(key)
                    current.left.parent = current
                    self._splay(current.left)
                    return
            elif key > current.key:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(key)
                    current.right.parent = current
                    self._splay(current.right)
                    return
            else:
                return  # Key already exists, no need to insert again

    def find(self, key):
        current = self.root
        while current:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                self._splay(current)
                return current
        return None

    def delete(self, key):
        node = self.find(key)
        if not node:
            return False

        self._splay(node)

        if not node.left:
            self.root = node.right
            if self.root:
                self.root.parent = None
        elif not node.right:
            self.root = node.left
            if self.root:
                self.root.parent = None
        else:
            left_max = self._subtree_max(node.left)
            if left_max.parent != node:
                left_max.parent.right = left_max.left
                if left_max.left:
                    left_max.left.parent = left_max.parent
                left_max.left = node.left
                left_max.left.parent = left_max
            left_max.right = node.right
            left_max.right.parent = left_max
            self.root = left_max
            self.root.parent = None

        return True

    def _subtree_max(self, node):
        current = node
        while current.right:
            current = current.right
        return current

    def inorder_traversal(self):
        def _inorder(node):
            if node:
                _inorder(node.left)
                print(node.key, end=' ')
                _inorder(node.right)

        _inorder(self.root)
        print()


# Example usage:
splay_tree = SplayTree()
splay_tree.insert(10)
splay_tree.insert(5)
splay_tree.insert(15)
splay_tree.insert(7)
splay_tree.insert(12)

print("Inorder traversal before delete:")
splay_tree.inorder_traversal()  # Output: 5 7 10 12 15

splay_tree.delete(10)

print("Inorder traversal after delete:")
splay_tree.inorder_traversal()  # Output: 5 7 12 15
