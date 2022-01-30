class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_mirror(r_a, r_b):
    if r_a == r_b is None:
        return True
    if r_a.data == r_b.data:
        return is_mirror(r_a.left, r_b.right) and is_mirror(r_a.right, r_b.left)


def is_symmetric(r):
    return is_mirror(r, r)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    print(is_symmetric(root))
