from binary_tree import BinaryTree
from typing import Union

def invert_binary_tree(root: BinaryTree) -> BinaryTree:
    """
    invert_binary_tree: inverts all the nodes in the binary tree & then returns the root node.

    O(T) -> O(N)
    O(S) -> O(log(N))
    """
    def invert(node: Union[BinaryTree, None]):
        if node is None:
            return

        node.left, node.right = (node.right, node.left)

        invert(node.left)
        invert(node.right)

    invert(root)

    return root
