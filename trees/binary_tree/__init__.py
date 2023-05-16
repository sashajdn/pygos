from typing import Union

class BinaryTree:
    def __init__(self, value: int):
        self._value = value
        self.left: Union[None, BinaryTree] = None
        self.right: Union[None, BinaryTree] = None

    def value(self) -> int:
        return self._value
