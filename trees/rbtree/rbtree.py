from abc import ABC, abstractmethod
from enum import Enum
from typing import Generator, Optional


class Color(Enum):
    """Color:"""

    RED = "red"
    BLACK = "black"


class Orientation(Enum):
    """Orientation:"""

    RR = "right-right"
    LL = "left-left"
    RL = "right-left"
    LR = "left-right"


class RBTree(ABC):
    """RBTree:"""

    @abstractmethod
    def insert(self, key, value):
        """Insert"""

    @abstractmethod
    def delete(self):
        """Delete"""

    @abstractmethod
    def exists(self, key) -> Optional["RBTree"]:
        """Exists."""

    @abstractmethod
    def get_min(self):
        """Get min."""

    @abstractmethod
    def get_max(self):
        """Get max."""

    @abstractmethod
    def inorder_travseral(self) -> Generator[Optional["RBTree"], None, None]:
        """Inorder traversal of the tree."""


class InstrusiveRBTree(RBTree):
    """InstrusiveRBTree:"""

    def __init__(self, color, key, value, parent):
        # If this is None, then we know for a fact that it is the root of the tree.
        self.parent = parent
        self.left = None
        self.right = None
        self.color = color
        self.key = key
        self.value = value

    def insert(self, key, value):
        inserted_node = self._insert(key, value)
        self._rebalance(inserted_node)

    def delete(self):
        pass

    def exists(self, key):
        if self.key == key:
            return self

        if self.left is None and self.right is None:
            return None

        if self.left is not None and key < self.left.key:
            return self.left.exists(key)

        if self.right is not None:
            return self.right.exists(key)

        return None

    def get_min(self):
        curr_node = self
        while curr_node.left is not None:
            curr_node = curr_node.left

        return curr_node.key

    def get_max(self):
        curr_node = self
        while curr_node.right is not None:
            curr_node = curr_node.right

        return curr_node.key

    def inorder_travseral(self):
        def _traverse(node):
            if node is not None:
                yield from _traverse(node.left)
                yield node
                yield from _traverse(node.right)

        return _traverse(self)

    def _rebalance(self, node_to_rebalance_from):
        parent = node_to_rebalance_from.parent
        # Root node case.
        if parent is None:
            return

        # Black parent with Red child satisfies the properties of RBTree,
        # since we assume None nodes are also black.
        if parent.color == Color.BLACK:
            return

        # At this point we know the parent is Red and *will* violate the properties unless we rotate
        # since we have a Red child.
        grandparent = parent.parent
        if grandparent is None:
            return

        uncle, orientation = self._fetch_uncle(node_to_rebalance_from)

        # Both uncle & parent are now colored red, we can color both Black & recurse up the
        # tree from the grandparent node.
        if uncle.color == Color.RED:
            uncle.color = Color.BLACK
            parent.color = Color.BLACK

            self._rebalance(parent.parent)
            return

        # In this case, the uncle is Black and the parent is Red.
        # Now we must perform a rotation depending on the orientation of the nodes.
        if orientation == Orientation.LL:
            self._rotate_right(grandparent)
            parent.Color, grandparent.Color = Color.BLACK, Color.RED
            return

        if orientation == Orientation.RR:
            self._rotate_left(grandparent)
            parent.Color, grandparent.Color = Color.BLACK, Color.RED
            return

        if orientation == Orientation.RL:
            self._rotate_right(parent)
            self._rotate_left(grandparent)
            self.color, grandparent.color = Color.RED, Color.BLACK
            return

        if orientation == Orientation.LR:
            self._rotate_left(parent)
            self._rotate_right(grandparent)
            self.color, grandparent.color = Color.RED, Color.BLACK
            return

        self._rebalance(parent)

    def _fetch_uncle(self, node):
        parent = node.parent
        grandparent = parent.parent
        uncle = (
            grandparent.right if grandparent.right is not parent else grandparent.left
        )

        if grandparent.left is parent and parent.left is node:
            return uncle, Orientation.LL

        if grandparent.right is parent and parent.right is node:
            return uncle, Orientation.RR

        if grandparent.right is parent and parent.left is node:
            return uncle, Orientation.RL

        return uncle, Orientation.LR

    def _rotate_left(self, u):
        v = u.right
        u.right = v.left

        if v.left is not None:
            v.left.parent = u

        v.parent = u.parent
        if u.parent is not None:
            if u.parent.right == u:
                u.parent.right = v
            else:
                u.parent.left = v

        v.left, u.parent = u, v

    def _rotate_right(self, u):
        v = u.left
        u.left = v.right

        if v.right is not None:
            v.right.parent = u

        v.parent = u.parent
        if u.parent is not None:
            if u.parent.left == u:
                u.parent.left = v
            else:
                u.parent.right = v

        v.right, u.parent = u, v

    def _insert(self, key, value):
        if key >= self.key:
            if self.right is None:
                self.right = self.__class__(Color.RED, key, value, self)
                return self.right

            self.right._insert(key, value)
            return self.right

        if self.left is None:
            self.left = self.__class__(Color.RED, key, value, self)
            return self.left

        self.left._insert(key, value)
        return self.left


if __name__ == "__main__":
    root = InstrusiveRBTree(Color.BLACK, 10, 0, None)

    root.insert(1, 100)
    root.insert(2, 101)
    root.insert(5, 102)
    root.insert(4, 103)
    root.insert(3, 104)

    exists = root.exists(4)
    if exists is not None:
        assert exists.key == 4

    min_so_far = root.get_min()
    assert min_so_far == 1

    max_so_far = root.get_max()
    assert max_so_far == 10

    root.insert(30, 105)
    max_so_far = root.get_max()
    assert max_so_far == 30

    inorder_traversal = [
        node.key for node in root.inorder_travseral() if node is not None
    ]

    assert inorder_traversal == [1, 2, 3, 4, 5, 10, 30]
