class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f'Node({self.value})'


class BinarySearchTree:
    def __init__(self, root: Node):
        self.root = root

    def find(self, value):
        result = self._rec_find(value, self.root)
        if result:
            return result
        else:
            print('There is no such value in a tree')

    def _rec_find(self, value, node: Node):
        if node is None:
            return False
        print(f'Заходим в {node}')
        if node.value == value:
            return node
        elif value < node.value:
            return self._rec_find(value, node.left)
        else:
            return self._rec_find(value, node.right)

    def insert(self, value):
        return self._rec_insert(value, self.root)

    def _rec_insert(self, value, node: Node):
        if value < node.value:
            if node.left:
                return self._rec_insert(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right:
                return self._rec_insert(value, node.right)
            else:
                node.right = Node(value)

    def find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete(self, value):

        # return self._rec_delete(value, self.root)
        # Search for the node to be deleted
        if value < self.root.value:
            self.root.left = self.delete(self.root.left, value)
        elif value > self.root.value:
            self.root.right = self.delete(self.root.right, value)
        else:
            # Node with only one child or no child
            if self.root.left is None:
                return self.root.right
            elif self.root.right is None:
                return self.root.left

            # Node with two children: Get the in-order successor
            temp = self.find_min(self.root.right)

            # Copy the in-order successor's content to this node
            self.root.value = temp.value

            # Delete the in-order successor
            self.root.right = self.delete(self.root.right, temp.key)

        return self.root

    # def _rec_delete(self, value, node: Node):
    #     to_del = None
    #     if value < node.value:
    #         if node.left.value == value:
    #             to_del = node.left
    #     else:
    #         if node.right.value == value:
    #             to_del = node.right
    #     if to_del:
    #         if to_del.left is None and to_del.


# nodes = [Node(4), Node(2), Node(3), Node(1), Node(6), Node(5), Node(7)]
# nodes[0].left = nodes[1]
# nodes[0].right = nodes[4]
# nodes[1].right = nodes[2]
# nodes[1].left = nodes[3]
# nodes[4].left = nodes[-2]
# nodes[4].right = nodes[-1]


bst = BinarySearchTree(Node(9))
bst.insert(7)
bst.insert(6)
bst.insert(5)
bst.insert(4)
bst.insert(3)
bst.insert(2)
bst.insert(1)

print(bst.find(1))

# list insert - O(n), find - O(n), del - O(n)
# BST  insert - O(log(n)), find - O(log(n)), del - O(log(n))
