class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def intersect(self, other):
        return not (self.x2 < other.x1 or self.x1 > other.x2 or
                    self.y2 < other.y1 or self.y1 > other.y2)

    def area(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1)


class Node:
    def __init__(self, is_leaf=True):
        self.is_leaf = is_leaf
        self.children = []
        self.rectangles = []


class RTree:
    def __init__(self, max_children=4):
        self.max_children = max_children
        self.root = Node()

    def insert(self, rectangle):
        node = self.choose_leaf(self.root, rectangle)
        node.rectangles.append(rectangle)
        if len(node.rectangles) > self.max_children:
            self.split(node)

    def choose_leaf(self, node, rectangle):
        if node.is_leaf:
            return node

        min_increase = float('inf')
        next_node = None
        for child in node.children:
            increase = self.enlargement(child, rectangle)
            if increase < min_increase:
                min_increase = increase
                next_node = child

        return self.choose_leaf(next_node, rectangle)

    def enlargement(self, node, rectangle):
        enlarged = Rectangle(min(node.rectangles[0].x1, rectangle.x1),
                             min(node.rectangles[0].y1, rectangle.y1),
                             max(node.rectangles[0].x2, rectangle.x2),
                             max(node.rectangles[0].y2, rectangle.y2))
        return enlarged.area() - node.rectangles[0].area()

    def split(self, node):
        axis = 0 if len(node.rectangles[0]) == 2 else 1
        node.rectangles.sort(key=lambda rect: (rect.x1, rect.y1)[axis])

        m = len(node.rectangles) // 2
        left_node = Node(is_leaf=node.is_leaf)
        right_node = Node(is_leaf=node.is_leaf)

        left_node.rectangles = node.rectangles[:m]
        right_node.rectangles = node.rectangles[m:]

        node.rectangles = []
        node.children = [left_node, right_node]

    def search(self, rectangle):
        return self.search_recursive(self.root, rectangle)

    def search_recursive(self, node, rectangle):
        results = []
        if node.is_leaf:
            for rect in node.rectangles:
                if rect.intersect(rectangle):
                    results.append(rect)
            return results

        for child in node.children:
            if child.rectangles:
                if child.rectangles[0].intersect(rectangle):
                    results.extend(self.search_recursive(child, rectangle))
        return results


# Example usage:
rtree = RTree()
rectangles = [Rectangle(0, 0, 2, 2), Rectangle(1, 1, 3, 3), Rectangle(4, 4, 6, 6)]
for rect in rectangles:
    rtree.insert(rect)

search_rect = Rectangle(1.5, 1.5, 5, 5)
search_results = rtree.search(search_rect)
for result in search_results:
    print(f"Rectangle intersecting search area: ({result.x1}, {result.y1}) - ({result.x2}, {result.y2})")
