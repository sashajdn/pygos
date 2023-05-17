from typing  import List, Optional

from binary_tree import BinaryTree

def maximum_binary_tree_depth_dfs(root: Optional[BinaryTree]) -> int:
    """
    maximum_binary_tree_depth_dfs: returns the number of nodes traversed along the longest path using dfs

    O(T): O(N)
    O(S): O(N) in the worst case if the binary tree in unbalanced, otherwise O(log(N)) if balanced.
    """
    if root == None:
        return 0

    return max(maximum_binary_tree_depth_dfs(root.left), maximum_binary_tree_depth_dfs(root.right)) + 1

def maximum_binary_tree_depth_bfs(root: Optional[BinaryTree]) -> int:
    """
    maximum_binary_tree_depth_bfs: returns the number of nodes traversed along the longest path using bfs

    O(T): O(N)
    O(S): O(N) in the worst case if the binary tree in unbalanced, otherwise O(log(N)) if balanced.
    """
    if root == None:
        return 0

    max_depth = 0
    queue: List[nodeWithDepth] = [nodeWithDepth(node=root, depth=1)]

    while len(queue) != 0:
        node = queue.pop(0)
        max_depth = max(max_depth, node.depth)

        if node.node.left != None:
            queue.append(nodeWithDepth(node.node.left, node.depth + 1))

        if node.node.right != None:
            queue.append(nodeWithDepth(node.node.right, node.depth + 1))

    return max_depth


class nodeWithDepth:
    def __init__(self, node: BinaryTree, depth: int):
        self.node = node
        self.depth = depth
