import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def eval_expression(node):
    # base case
    if node.left == node.right is None:
        return node.data
    # recursive case
    else:
        return ops[node.data](eval_expression(node.left), eval_expression(node.right))


if __name__ == "__main__":
    root = TreeNode('+')
    root.left = TreeNode('*')
    root.right = TreeNode('-')
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(100)
    root.right.right = TreeNode('/')
    root.right.right.left = TreeNode(20)
    root.right.right.right = TreeNode(2)

    print(eval_expression(root))
