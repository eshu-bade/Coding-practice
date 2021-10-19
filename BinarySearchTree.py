"""
Binary search tree has left and right subtrees.
If the new child is smaller than node, it must go left side
If the new child is greater than node, it must go right side

It has 3 types of sortings
 - In-order traversal method: returns list of elements in a binary tree in a specific order(first visits leftsubtree
 - Out-order traversal method


"""


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):

        if data == self.data:  # To check if the new value already exists
            return
        if data < self.data:  # add data to left subtree
            if self.left:  # If tree is not empty
                self.left.addChild(data)
            else:  # If tree is empty
                self.left = BinarySearchTreeNode(data)
        else:  # add data to right subtree
            if self.right:  # If tree is not empty
                self.right.addChild(data)
            else:  # If tree is not empty
                self.right = BinarySearchTreeNode(data)

    def inOrderTraversal(self):
        listElements = []
        if self.left:
            listElements += self.left.inOrderTraversal()

        listElements.append(self.data)

        if self.right:
            listElements += self.right.inOrderTraversal()

        return listElements

    def post_order_traversal(self):
        listElements = []
        if self.left:
            listElements += self.left.post_order_traversal()
        if self.right:
            listElements += self.right.post_order_traversal()

        listElements.append(self.data)

        return listElements

    def pre_order_traversal(self):
        listElements = [self.data]
        if self.left:
            listElements += self.left.pre_order_traversal()
        if self.right:
            listElements += self.right.pre_order_traversal()

        return listElements

    def searchValue(self, value):
        if self.data == value:
            return "Value exists"
        if value < self.data:
            if self.left:
                return self.left.searchValue(value)
            else:
                return "Value doesn't exist"
        if value > self.data:
            if self.right:
                return self.right.searchValue(value)
            else:
                return "Value doesn't exists"

    def findMini(self):
        if self.left is None:
            return self.data
        return self.left.findMini()

    def findMax(self):
        if self.right is None:
            return self.data
        return self.right.findMax()

    def calculateSum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum


def buildTree(listElements):
    root = BinarySearchTreeNode(listElements[0])
    for i in range(1, len(listElements)):
        root.addChild(listElements[i])
    return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbersTree = buildTree(numbers)
    # print(numbersTree.searchValue(23))
    print(numbersTree.findMini())
    print(numbersTree.findMax())
    print(numbersTree.searchValue(30))
