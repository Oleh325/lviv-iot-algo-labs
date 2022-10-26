class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
 
class AVL_Tree():
    def delete(self, root, key):

        if not root:
            return root
 
        elif key < root.value:
            root.left = self.delete(root.left, key)
 
        elif key > root.value:
            root.right = self.delete(root.right, key)
 
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
 
            elif root.right is None:
                temp = root.left
                root = None
                return temp
 
            temp = self.getMinNode(root.right)
            root.value = temp.value
            root.right = self.delete(root.right,
                                      temp.value)
 
        if root is None:
            return root
 
        self.recalculateHeight(root)
 
        return self.balanceTree(root)
 
    def balanceTree(self, root):
        balance_factor = self.getBalanceFactor(root)

        # LL rotation
        if balance_factor > 1 and self.getBalanceFactor(root.left) >= 0:
            return self.rightRotate(root)
 
        # RR rotation
        if balance_factor < -1 and self.getBalanceFactor(root.right) <= 0:
            return self.leftRotate(root)
 
        # LR rotation
        if balance_factor > 1 and self.getBalanceFactor(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        # RL rotation
        if balance_factor < -1 and self.getBalanceFactor(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root

    def recalculateHeight(self, root):
            root.height = 1 + max(self.getHeight(root.left),
                        self.getHeight(root.right))

    def leftRotate(self, first_node):
        second_node = first_node.right
        child_tree = second_node.left
 
        second_node.left = first_node
        first_node.right = child_tree
 
        self.recalculateHeight(first_node)
        self.recalculateHeight(second_node)
 
        return second_node
 
    def rightRotate(self, first_node):
        second_node = first_node.left
        child_tree = second_node.right
 
        second_node.right = first_node
        first_node.left = child_tree
 
        self.recalculateHeight(first_node)
        self.recalculateHeight(second_node)

        return second_node
 
    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
 
    def getBalanceFactor(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)
 
    def getMinNode(self, root):
        if root is None or root.left is None:
            return root
 
        return self.getMinNode(root.left)

    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        self.recalculateHeight(root)
        balance_factor = self.getBalanceFactor(root)
        if balance_factor > 1 and key < root.left.value:
            return self.rightRotate(root)
        if balance_factor < -1 and key > root.right.value:
            return self.leftRotate(root)
        if balance_factor > 1 and key > root.left.value:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance_factor < -1 and key < root.right.value:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root
 
    def printTree(self, root):
        count = 0
        nodes = []
        nodes.append(root)
        for node in nodes:
            if node is not None:
                print(str(node.value) + " ", end="")
                if node.left or node.right:
                    nodes.append(node.left)
                    nodes.append(node.right)
            else:
                print("X ", end="")
            elemsInARow = 0
            while elemsInARow < count:
                elemsInARow = elemsInARow*2 + 2
            if count == elemsInARow:
                print()
            count += 1
            
 
 
testTree = AVL_Tree()
root = None
values = [9, 5, 10, 0, 6, 11, -1, 1, 2, 4, 8, 7, 16, 23]
 
for value in values:
    root = testTree.insert(root, value)
 
print("Before deletion: ")
testTree.printTree(root)
print()
 
root = testTree.delete(root, 9)

print("After deletion: ")
testTree.printTree(root)