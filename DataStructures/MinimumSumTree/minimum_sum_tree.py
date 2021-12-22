import sys


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def minimum_sum_tree(leaf_nodes_list):
    """ This function takes in an list containing the value of leaf nodes inorder traversal. The purpose of this
    function is to provide the sum of nodes of minimum sum tree.
    parameters:
        leaf_nodes_list: list containing the value of leaf nodes inorder traversal
    returns:
        sum_minimum_nodes: sum of nodes of minimum tree
    usage:
        minimum_sum_tree([6,2,4,8)
    """
    sum_minimum_nodes = leaf_nodes_list[0]  # initialize minimum nodes sum to 0.
    root_node = TreeNode(leaf_nodes_list[0])  # if first leaf node inorder traversal then make a new TreeNode
    temp_max = leaf_nodes_list[0]  # temporary max variable to hold value of maximum value node on left part of sub tree

    for i in range(1, len(leaf_nodes_list)):
        new_root_node = TreeNode(leaf_nodes_list[i] * temp_max)  # make NEW root node one level above the root node.
        sum_minimum_nodes += new_root_node.data
        new_root_node.left = root_node  # make old root node as the left part of NEW root node.
        new_root_node.right = TreeNode(leaf_nodes_list[i])  # make the ip node val as right side of NEW root node.
        sum_minimum_nodes += new_root_node.right.data
        root_node = new_root_node

        # update temp_max variable in case the input node value is greater than old maximum value.
        if temp_max < leaf_nodes_list[i]:
            temp_max = leaf_nodes_list[i]
    return sum_minimum_nodes


if __name__ == "__main__":

    list_of_lists = []  # this list of list will store all the lines of input txt file in lists
    try:
        with open('inputPS3.txt') as f_read, open('outputPS3.txt', 'w+') as f_write:
            for line in f_read:
                # each inner list contains leaf nodes of a binary tree inorder traversal.
                inner_list = [int(elt.strip()) for elt in line.split(' ')]

                # Check if there is any negative in the input file and raise exception
                res = any(elt < 0 for elt in inner_list)
                if res:
                    print("Negative numbers are not allowed in the input file. Please re-run after modifying the file.")
                    sys.exit(1)

                f_write.write(str(minimum_sum_tree(inner_list)) + '\n')  # write sum of nodes of min tree to O/P file.

    # Raise exception in case input file is missing.
    except FileNotFoundError as error:
        print("File inputPS3.txt is not present in path where this python program is placed. Please re-run"
              " the program after placing the input file.")
        sys.exit(1)
