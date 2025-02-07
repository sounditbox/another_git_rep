class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        self.height = 1

    def __repr__(self):
        return f'({self.data})'


class AVLTree:

    def __init__(self):
        self.root = None

    def insert_node(self, root, value):

        if not root:
            return Node(value)
        elif value < root.data:
            root.left = self.insert_node(root.left, value)
        elif value > root.data:
            root.right = self.insert_node(root.right, value)
            root.height = 1 + max(self.avl_Height(root.left),
                                  self.avl_Height(root.right))
            root = self.balance(root, value)
            return self.leftRotate(root)
        return root

    def delete_node(self, root, value):
        if not root:
            return
        elif value < root.data:
            root.left = self.delete_node(root.left, value)
        elif value > root.data:
            root.right = self.delete_node(root.right, value)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.avl_MinValue(root.right)
            root.data = temp.data
            root.right = self.delete_node(root.right, temp.data)
        if root is None:
            return root

        root.height = 1 + max(self.avl_Height(root.left),
                              self.avl_Height(root.right))

        root = self.balance(root, value)

        return root

    def balance(self, root, value):

        balance_factor = self.avl_BalanceFactor(root)

        if balance_factor > 1:
            if value < root.left.data:
                if self.avl_BalanceFactor(root.left) >= 0:
                    return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balance_factor < -1:
            if value > root.right.data:
                return self.rightRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def avl_MinValue(self, root):
        if root is None or root.left is None:
            return root
        return self.avl_MinValue(root.left)

    def avl_Height(self, root):
        if not root:
            return 0
        return root.height

    def avl_BalanceFactor(self, root):
        if not root:
            return
        return self.avl_Height(root.left) - self.avl_Height(root.right)

    def leftRotate(self, root):
        a = root.right
        root.right = a.left
        a.left = root

        root.height = 1 + max(self.avl_Height(root.left),
                              self.avl_Height(root.right))
        a.height = 1 + max(self.avl_Height(a.left),
                           self.avl_Height(a.right))

        return a

    def rightRotate(self, root):
        a = root.left
        root.left = a.right
        a.right = root

        root.height = 1 + max(self.avl_Height(root.left),
                              self.avl_Height(root.right))
        a.height = 1 + max(self.avl_Height(a.left),
                           self.avl_Height(a.right))
        return a

    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.data), end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)


Tree = AVLTree()
root = None
root = Tree.insert_node(root, 40)
root = Tree.insert_node(root, 60)
root = Tree.insert_node(root, 50)
root = Tree.insert_node(root, 20)
root = Tree.delete_node(root, 40)

Tree.preOrder(root)
