class Solution:
    def isValidBST(self, root):
        values = []

        def inorder(node):
            if node is None:
                return 0

            inorder(node.left)
            values.append(node.val)
            inorder(node.right)
        inorder(root)

        for i in range(1, len(values)):
            if values[i] <= values[i - 1]:
                return False
        return True